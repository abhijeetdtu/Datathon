# %%
import pandas as pd
import re
import os

from Datathon.Utils.getData import  *

from scipy.stats import chi2_contingency
# %%

path = os.path.abspath(os.path.join(os.path.dirname("__file__")  , "Datathon" , "Data", "training_v2.csv"))
df = pd.read_csv(path)
# %%

# %% markdown
# # Columns Available
# %%
print(list(df.columns))
# %% markdown
# ## Columns that are not a reading
# %%
cols_notareading = [c for c in df.columns if len(re.findall("(min|max|apache)",  c)) == 0]
print(cols_notareading)
# %%
cols_diseases = cols_notareading[cols_notareading.index("aids"):] + ["elective_surgery" ]
print(cols_diseases)
# %% markdown
# # Missing Values
# %% markdown
# These have more than 80 % missing values
# %%

nacounts = df.isna().sum()
cols_extmiss = list(nacounts[nacounts.sort_values() > df.shape[0]*0.8].index)
print(cols_extmiss)

# %% markdown
# # Disease Counts
# %%

tdf = df[cols_diseases + ["encounter_id"]].melt( value_vars =cols_diseases)
tdf["value"].sum()

# %% markdown
# Only 45K rows for these diseases
# Are there any other disease missed
# %%

tdf[tdf["value"] == 0].shape
tdf[tdf["value"] != 0].shape

df[df[cols_extmiss].any(1)].shape


df["icu_stay_type"].unique()

pd.crosstab(df["icu_stay_type"] , df["hospital_death"])


kdf = df
for cold in cols_diseases:
    for colmiss in cols_extmiss:
        ct = pd.crosstab(kdf[cold] , kdf[colmiss].isna())
        c2t = chi2_contingency(ct)
        if c2t[1] < 0.01:
            print(f"{cold} : {colmiss} : {c2t[1]}")

# %%
df[cols_extmiss + ["hospital_death"]]


# %% markdown
# # Which type of columns have most missing Values
# %%
cols_demo = getColumnsByType("demographic")
'icu_admit_type' in df.columns
set(cols_demo).difference(set(df.columns))

cols_demo = list(set(cols_demo).intersection(set(df.columns)))

df[cols_demo].isna().
