import pandas as pd

#df = pd.read_csv('Maryland crab sheet cs.csv')
#df = pd.read_csv('North Carolina Crabs.csv')
#print(df)
marylandCrab = "data/maryland_crab.csv"
northCarolinaCrab = "data/north_carolina_crabs.csv"

def ingestCSV (fileName):
    df = pd.read_csv(fileName)

    return df

marylandDF = ingestCSV(marylandCrab)
northCarolinaDF = ingestCSV(northCarolinaCrab)

