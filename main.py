import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from visuals import graphs
from etl import extract
from analysis import models

#new test

#Choose a state to generate visuals for
mdCrabs = extract.ingestCSV("data/graph/mdGraph.csv")
mdYears = extract.ingestCSV("data/cleaned/mdDropped.csv")


#Trouble importing from models.py will fix
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

#Get column data as lists
crabList = getColumn(mdCrabs,"Crabs")
yearList = getColumn(mdYears,"Survey Year (Year Survey Ended)")

#Plot data
#years for x axis, population for y axis
##Important to exclude first year becasue the percentages are values of change between 2 years
graphs.lineGraph(yearList[1:],crabList)







