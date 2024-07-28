import pandas as pd
import numpy as np
#test
nc = pd.read_csv("data/ncDropped.csv")
md = pd.read_csv("data/mdDropped.csv")
ncColumnName = "Total Catch"
mdColumnName = "Total Number of Crabs in Millions (All Ages)" 
def getColumn (df,columnName):
    df = df.get(columnName) 
    list = df.to_list()
    return list

ncList = getColumn(nc, ncColumnName)
mdList = getColumn(md,mdColumnName)
#print(ncList)
#print(mdList)

def percentChange (list):
    myArray = np.array(list)
    myPercents = np.diff(myArray)/myArray[:-1]*100
    myMax = np.max(np.abs(myPercents))
    #myMin = np.min(np.abs(myPercents))
    return myMax, myPercents

mdStats = percentChange(mdList)
ncStats = percentChange(ncList)
#print(mdStats)
#print(ncStats)

