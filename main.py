import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from visuals import graphs
from etl import extract
from analysis import models
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main ():
    #Choose a state to generate visuals for
    mdCrabs = extract.ingestCSV("data/graph/mdGraph.csv")
    mdYears = extract.ingestCSV("data/cleaned/mdDropped.csv")


    #Get column data as lists
    crabList = models.getColumn(mdCrabs,"Crabs")
    yearList = models.getColumn(mdYears,"Year")

    #Plot data
    #years for x axis, population for y axis
    ##Important to exclude first year becasue the percentages are values of change between 2 years
    graphs.lineGraph(yearList[1:],crabList)
    
    #Linear regression testing
    df = pd.read_csv("data/cleaned/mergedData.csv")
    df.drop(df.tail(1).index,inplace=True)
    graphs.linearRegressionTest(df,"Annual","Total Number of Crabs in Millions (All Ages)")

x = main()
print(x)






