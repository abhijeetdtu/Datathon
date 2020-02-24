%load_ext autoreload
%autoreload 2
%matplotlib inline

import xgboost as xgb

from sklearn.decomposition import PCA
from Datathon.Utils.apache2Calc import *
from Datathon.Utils.getData import *
from Datathon.Utils.pipeFunctions import *
from sklearn.preprocessing import StandardScaler
from plotnine import *
#df = getTrainingData()

adf = getTrainingData()

df= adf.copy()
numeric_cols = getNumericColumns(df)
cat_cols = getCategorialColumns(df)

#from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer

num_mean = SimpleImputer(strategy="mean")
df.loc[:,numeric_cols] = num_mean.fit_transform(df.loc[:,numeric_cols])

cat_freq = SimpleImputer(strategy="most_frequent")
df.loc[:,cat_cols] = cat_freq.fit_transform(df.loc[:,cat_cols])

df.iloc[32][df.iloc[32].isna()==True]

def getAPACHEScore(row):
    cols = {
        "age" : row["age"],
        "temperature" : row["temp_apache"],
        "heart_bpm": row["heart_rate_apache"],
        "respiratory_rate": row["resprate_apache"],
        "oxygenation": row["pao2_apache"],
        "ph": row["ph_apache"],
        "sodium": row["sodium_apache"],
        "hematocrit": row["hematocrit_apache"],
        "wbc": row["wbc_apache"],
    }
    return np.sum([calculate_single_scores(v,k) for k,v in cols.items()])


df["apacheScore"] = df.apply(getAPACHEScore , axis=1)

df["apacheScore"].describe()

import plotnine as p9

p9.ggplot(df , aes(x="apacheScore" , y="apache_4a_hospital_death_prob" , color="hospital_death")) + geom_point()
