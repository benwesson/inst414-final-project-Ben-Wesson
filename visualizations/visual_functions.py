
import pandas as pd
import numpy as np
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy







def lineGraph(df,col1,col2,graphTitle,xAxis,yAxis):
    """
    Produce a plotted line graph

    Parameters
    col1 : string
        string repersenting column in merged database.
    col2 : string
        string repersenting column in merged database.
    df : pandas dataframe
        Dataframe of merged values form the crab population and temperature csvs
    string : graphTitle
        Help you identify which coefficent in the terminal.
    xAxis : string 
        Label for graphs x axis
    yAxis
        Label for graphs y axis
    Returns
    figure : A plot showing a linegraph. It gets saved to data/visuals.
    """
        
    saveString = "data/visuals/" + graphTitle + ".png"
    sns.lineplot(x = col1,y = col2,data = df).set(title=graphTitle)
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.savefig(saveString)
    plt.show()