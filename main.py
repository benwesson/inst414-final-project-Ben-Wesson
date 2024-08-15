
from  etl.extract import ingestCSV
from etl.transform_and_load import dropColumns,convertData,mergeDf
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    #Load CSVs into dataframes.
    average_temperature_df = ingestCSV("data/raw/average_temperature.csv")
    maryland_crab_df = ingestCSV("data/raw/maryland_crab.csv")

    #Drop extra columns.
    maryland_crab_df_drop = dropColumns(maryland_crab_df,[2,3,4,5,6])
    #print(maryland_crab_df_drop)

    #Prepare for merge.
    maryland_crab_df_ready,average_temperature_df_ready = convertData(maryland_crab_df_drop,average_temperature_df)
     
    #Create merged dataframe.
    merged_df = mergeDf(maryland_crab_df_ready,average_temperature_df_ready)
    #print(merged_df)
    
    #Write the merged dataframe to the cleaned data folder
    merged_df.to_csv('data/cleaned/merged_data.csv',header=True, index=False)

    #Read in cleaned dataset
    merged_df = pd.read_csv("data/cleaned/merged_data.csv")

    def lineGraph(df,col1,col2,graphTitle,xAxis,yAxis):
        #graphData = sns.load_dataset(df)
        saveString = "data/visuals/" + graphTitle + ".png"
        sns.lineplot(x = col1,y = col2,data = df).set(title=graphTitle)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        plt.savefig(saveString)
        plt.show()

    lineGraph(merged_df,'Year','Annual','Year to Year Temperature Change In Maryland','Year','Mean Annual Temperature')





if __name__ == '__main__':
    main()

















"""
logger = logging.getLogger(__name__)
def main ():

    #Setup logger
    logging.basicConfig(filename='main.log', level=logging.INFO)
    logger.info('Started')
    mylib.do_something()
    logger.info('Finished') 
    logging.debug('Test')


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
    y = df['Total Number of Crabs in Millions (All Ages)'].to_list()
    x = df['Annual'].to_list()

    sns.set_style('whitegrid') 
    print(sns.lmplot(x ='Annual', y ='Total Number of Crabs in Millions (All Ages)', data = df))
   
    #plt.scatter(x, y)
    plt.show()
   



"""







