import pandas as pd
import numpy as np

#Read in the cleaned versions of the crab popualtion data
nc = pd.read_csv("data/ncDropped.csv")
md = pd.read_csv("data/mdDropped.csv")

#Varibles to pinpoint the columns that contain the total crab counts  
ncColumnName = "Total Catch"
mdColumnName = "Total Number of Crabs in Millions (All Ages)" 

def getColumn (df,columnName):
    """
    Crab Popualtion Count Locater

    Parameters
    df : pandas dataframe
        dataset on crab populations for a given year for a certain state.
    columnName : string
        name of the column in the dataset that has the crab population counts

    Returns
    list : The column of crab population count values as a list
    """
    df = df.get(columnName) 
    list = df.to_list()
    return list

#Call function for both states to get a list of crab popultions over the years
ncList = getColumn(nc, ncColumnName)
mdList = getColumn(md,mdColumnName)
#print(ncList)
#print(mdList)

def percentChange (list):
    """
    Crab Popualtion Count Locater

    Parameters
    df : pandas dataframe
        dataset on crab populations for a given year for a certain state.
    columnName : string
        name of the column in the dataset that has the crab population counts

    Returns
    list : The column of crab population count values as a list
    """
    myArray = np.array(list)
    myPercents = np.diff(myArray)/myArray[:-1]*100
    myMax = np.max(np.abs(myPercents))
    #myMin = np.min(np.abs(myPercents))
    return myMax, myPercents


mdStats = percentChange(mdList)
ncStats = percentChange(ncList)
#print(mdStats)
#print(ncStats)

