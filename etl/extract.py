import pandas as pd



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


