import pandas as pd

#CSV filenames to be used as parameters for ingestion function
marylandCrab = "data/raw/maryland_crab.csv"
northCarolinaCrab = "data/raw/north_carolina_crabs.csv"
mdTemp = "data/raw/md_avg.csv"

def ingestCSV (fileName):
    """
    CSV to pandas Dataframe Converter

    Parameters
    fileName : CSV file
        Dataset on crab populations for a given year for a certain state. 
    
    Returns
    df : A pandas dataframe of the CSV file ready for cleaning.
    """
    df = pd.read_csv(fileName)

    return df

#Call function for all datasets needed to prep for cleaning
marylandDF = ingestCSV(marylandCrab)
northCarolinaDF = ingestCSV(northCarolinaCrab)
mdTempDF = ingestCSV(mdTemp)
#print(marylandDF)

