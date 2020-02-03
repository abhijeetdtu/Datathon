import pandas as pd
import os
from pathlib import Path

cwd = Path().resolve()
cwd

pathToDataFolder =  os.path.abspath(os.path.join(cwd ,"Datathon", "Data"))
trainDataPath = os.path.abspath(os.path.join(pathToDataFolder, "training_v2.csv"))
path = os.path.abspath(os.path.join(pathToDataFolder, "WIDS Datathon 2020 Dictionary.csv"))
DICTDF = pd.read_csv(path)

DICTDF


DICTDF["Category"].unique()

DICTDF["Data Type"].unique()
DICTDF.groupby("Category").head(5)

def _columnDtypeCorrection(c):
    dtype = list(DICTDF[DICTDF["Variable Name"] == c]["Data Type"])[0]
    if c.find("_id") > -1:
        dtype = "binary"
    if c.find("bmi") > -1:
        dtype = "float"

    return dtype

def getTrainingData():
    df =  pd.read_csv(trainDataPath)
    for c in df.columns:
        dtype = _columnDtypeCorrection(c)
        if dtype == "string" or dtype == "binary":
            df[c] = df[c].astype("category")
        elif dtype == "integer" and len(df[c].unique()) < 5:
            df[c] = df[c].astype("category")
        else:
            df[c] = df[c].astype("float")
    return df



def getColumnTypes():
    return DICTDF["Category"].unique()


def getColumnsByType(type):
    return list(DICTDF[DICTDF["Category"] == type]["Variable Name"])

def getDependentVariable():
    return "hospital_death"

getColumnTypes()


getColumnsByType("demographic")

getTrainingData().columns
DICTDF[DICTDF["Variable Name"] == "bmi"]
