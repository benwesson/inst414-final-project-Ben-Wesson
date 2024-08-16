
import pandas as pd
import numpy as np
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from sklearn import linear_model




def regressionGraph(col1,col2,df,graphTitle,xAxis,yAxis):
    """
    Regression model plotter

    Parameters
    col1 : string
        string repersenting column in merged database.
    col2 : string
        string repersenting column in merged database.
    df : pandas dataframe
        Dataframe of merged values form the crab population and temperature csvs
    graphTitle : string
        Label for graphs title
    xAxis : string 
        Label for graphs x axis
    yAxis
        Label for graphs y axis

    
    Returns
    figure : A plot showing a regression model with line of best fit. It gets saved to data/visuals.
    """
    sns.regplot(x=col1,y=col2,data = df).set(title=graphTitle)
    saveString = "data/visuals/" + graphTitle + ".png"
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.savefig(saveString)
    plt.show()

def predictiveModel(col1,col2,df):
    """
    Make prediction about 2024 crab popualtion

    Parameters
    col1 : string
        string repersenting column in merged database.
    col2 : string
        string repersenting column in merged database.
    df : pandas dataframe
        Dataframe of merged values form the crab population and temperature csvs
    
    Returns
    float : prints a number in the terminal repersenting the estiamted crab count for 2024
    """
    varX = df[[col1,col2]]
    varY = df['Total Number of Crabs in Millions (All Ages)']
    sk_reg = linear_model.LinearRegression()
    sk_reg.fit(varX.values,varY.values)
    predCrabs = sk_reg.predict([[72.7,56.8]])
    print(predCrabs)

def correlationCoe(df,col1,col2,title):
      

    """
    Produce a correlation coefficent for a given plot

    Parameters
    col1 : string
        string repersenting column in merged database.
    col2 : string
        string repersenting column in merged database.
    df : pandas dataframe
        Dataframe of merged values form the crab population and temperature csvs
    string : title
        Help you identify which coefficent in the terminal.
    
    Returns
    string : prints a labelled coefficent to terminal.
    """
    x = df[col1].to_list()
    y = df[col2].to_list()
    r = np.corrcoef(x,y)
    print(title,  ":  ", r)