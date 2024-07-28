import extract
import pandas as pd

#Import the raw dataframes from the extract file. No changes have been made yet
md = extract.marylandDF
nc = extract.northCarolinaDF

#These lists repersent the columns I want to drop in the datasets
mdList = [2,3,4,5,6]
ncList = [1,2,3]

#Planned feature
#Add function to create mergerd CSV with shared years
#Convert to common units. 
#Not needed yet because I am at first focusing on measuirng percent change

def dropCommas (df):
    """
    Remove Commas from numbers in dataframes

    Parameters
    df : pandas dataframe
        dataset on crab populations for a given year for a certain state.
    
    Returns
    df : Datasest with numbers as integers 
    """
    df = df.replace(',','', regex=True)
    return df

def dropColumns (df,list):
    """
    Remove Commas from numbers in dataframes

    Parameters
    df : pandas dataframe
        dataset on crab populations for a given year for a certain state.
    
    Returns
    df : Datasest with numbers as integers 
    """
    
    df.drop(df.columns[list],axis = 1, inplace = True)
    return df

#Call function to drop commas in population numbers
mdComma = dropCommas(md)
ncComma = dropCommas(nc)

#Call function to drop columns that are not year or pop count
mdDrop = dropColumns(mdComma,mdList)
ncDrop = dropColumns(ncComma,ncList)

#Write cleaned dataframes to new CSVs
mdDrop.to_csv('mdDropped.csv',header=True, index=False)
ncDrop.to_csv('ncDropped.csv',header=True, index=False)

#print(mdDrop)
#print(ncDrop)

