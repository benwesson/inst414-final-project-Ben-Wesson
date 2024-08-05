
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


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
mergedMd = pd.read_csv("data/cleaned/mergedData.csv")
mergedMd.drop(mergedMd.tail(1).index,inplace=True)
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
#Uncomment to generate visuals
#ncGraph = lineGraph(ncYears[1:],ncCrabs)
#mdGraph = lineGraph(mdYears[1:],mdCrabs)

#print(mergedMd.dtypes)
#Sci kit learn

x = getColumn(mergedMd,"Annual")
x = np.array(x)
x = x.reshape(10,2)
y = getColumn(mergedMd,"Total Number of Crabs in Millions (All Ages)")
y = np.array(y)
y = y.reshape(10,2)
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=4, random_state=4,shuffle=False)

model = LinearRegression().fit(x_train, y_train)
model.intercept_
print(model.coef_)


print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

y_pred = model.predict(x_test)

plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()


