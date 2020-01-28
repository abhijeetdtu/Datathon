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


def getTrainingData():
    return pd.read_csv(trainDataPath)

def getColumnTypes():
    return DICTDF["Category"].unique()


def getColumnsByType(type):
    return list(DICTDF[DICTDF["Category"] == type]["Variable Name"])

getColumnTypes()


getColumnsByType("demographic")
