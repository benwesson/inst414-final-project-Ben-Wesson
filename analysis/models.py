
import pandas as pd
import numpy as np
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy
from sklearn import linear_model




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

def correlationCoe(df,col1,col2,title):
      x = df[col1].to_list()
      y = df[col2].to_list()
      r = np.corrcoef(x,y)
      print(title,  ":  ", r)