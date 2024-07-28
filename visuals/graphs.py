
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Load percent change data from analysis
#CSV filenames to be used as parameters for ingestion function
marylandCrab = "data/graph/mdGraph.csv"
northCarolinaCrab = "data/graph/ncGraph.csv"

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

#Read in the cleaned versions of the crab popualtion data
nc = pd.read_csv("data/cleaned/ncDropped.csv")
md = pd.read_csv("data/cleaned/mdDropped.csv")

#print(nc)

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


ncYears = getColumn(nc,"Year")
mdYears = getColumn(md,"Survey Year (Year Survey Ended)")
mdCrabs = getColumn(marylandDF,"Crabs")
ncCrabs = getColumn(northCarolinaDF,"Crabs")
print(ncCrabs)
print(ncYears)


def lineGraph(xAxis,yAxis):
    """
    Line Graph Plotter

    Parameters
    xAxis : integer list
        Years crab population was counted
    yAxis: integer lsit
        Crab count population for a given state

    Returns
    plot : line graph showing percent change in crab popultion size over years. 
    """
    #xValues = np.array(xAxis)
    #yValues = np.array(yAxis)
    plt.plot(xAxis,yAxis)
    plt.show()

#Important to exclude first year becasue the percentages are values of change between 2 years
ncGraph = lineGraph(ncYears[1:],ncCrabs)
mdGraph = lineGraph(mdYears[1:],mdCrabs)


