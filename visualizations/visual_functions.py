
import pandas as pd
import numpy as np
import scipy.stats
import seaborn as sns
import matplotlib.pyplot as plt
import scipy







def lineGraph(df,col1,col2,graphTitle,xAxis,yAxis):
        #graphData = sns.load_dataset(df)
        saveString = "data/visuals/" + graphTitle + ".png"
        sns.lineplot(x = col1,y = col2,data = df).set(title=graphTitle)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        plt.savefig(saveString)
        plt.show()