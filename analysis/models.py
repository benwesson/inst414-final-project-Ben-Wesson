
import pandas as pd
import numpy as np
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from sklearn import linear_model

def lineGraph(df,col1,col2,graphTitle,xAxis,yAxis):
        #graphData = sns.load_dataset(df)
        saveString = "data/visuals/" + graphTitle + ".png"
        sns.lineplot(x = col1,y = col2,data = df).set(title=graphTitle)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        plt.savefig(saveString)
        plt.show()


def regressionGraph(col1,col2,df,graphTitle,xAxis,yAxis):
    sns.regplot(x=col1,y=col2,data = df).set(title=graphTitle)
    saveString = "data/visuals/" + graphTitle + ".png"
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.savefig(saveString)
    plt.show()

def predictiveModel(col1,col2,df):
      varX = df[[col1,col2]]
      varY = df['Total Number of Crabs in Millions (All Ages)']
      sk_reg = linear_model.LinearRegression()
      sk_reg.fit(varX.values,varY.values)
      predCrabs = sk_reg.predict([[72.7,56.8]])
      print(predCrabs)