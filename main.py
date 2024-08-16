
from  etl.extract import ingestCSV
from etl.transform_and_load import dropColumns,convertData,mergeDf
from analysis.models import regressionGraph,predictiveModel,correlationCoe
from visualizations.visual_functions import lineGraph
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import logging


logger = logging.getLogger(__name__)
def main():

    #Logger
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger.info('Started')
    
    
    #Load CSVs into dataframes.
    average_temperature_df = ingestCSV("data/raw/average_temperature.csv")
    maryland_crab_df = ingestCSV("data/raw/maryland_crab.csv")
    crab_prices_df = ingestCSV("data/raw/crab_prices.csv")
    logger.info('Save files a dataframes')

    #Drop extra columns.
    maryland_crab_df_drop = dropColumns(maryland_crab_df,[2,3,4,5,6])
    #print(maryland_crab_df_drop)
    logger.info('drop columns from datasets')

    #Prepare for merge.
    maryland_crab_df_ready,average_temperature_df_ready = convertData(maryland_crab_df_drop,average_temperature_df)
    logger.info('Dataframes now contain all numeric data')

    #Create merged dataframe.
    merged_df = mergeDf(maryland_crab_df_ready,average_temperature_df_ready)
    #print(merged_df)
    logger.info('Merge crab and temperature dataframe')

    #Write the merged dataframe to the cleaned data folder
    merged_df.to_csv('data/cleaned/merged_data.csv',header=True, index=False)
    logger.info('Save merged dataframe to data/cleaned')
    #Read in cleaned dataset
    merged_df = pd.read_csv("data/cleaned/merged_data.csv")
    logger.info('read in cleaned dataset')
    #Generate line graphs
    lineGraph(merged_df,'Year','Annual','Year to Year Temperature Change In Maryland','Year','Mean Annual Temperature(Fahrenheit)')
    lineGraph(merged_df,'Year','Total Number of Crabs in Millions (All Ages)','Year to Year Chesapeake Bay Crab Population Change','Year','Crabs(Millions)')
    lineGraph(crab_prices_df,'Year','Blue Crab Dockside Value(Adjusted Millions)','Change in Maryland Blue Crab Dockside Value Adjusted for Inflation','Year','Blue Crab Dockside Value(Millions)')
    logger.info('Basic line graphs generated')

    #Generate regression graphs
    regressionGraph("Annual","Total Number of Crabs in Millions (All Ages)",merged_df,"Total Number of Crabs in Millions vs Mean Annual Temperature In Maryland",'Mean Annual Temperature(Fahrenheit)',"Crabs(Millions)")
    r = correlationCoe(merged_df,"Annual","Total Number of Crabs in Millions (All Ages)","Total Number of Crabs in Millions vs Mean Annual Temperature In Maryland")
    logger.info(f"Annual: {r}")
    print(r)

    regressionGraph("Winter(Dec-Feb)","Total Number of Crabs in Millions (All Ages)",merged_df,"Total Number of Crabs in Millions vs Mean Winter Temperature In Maryland",'Mean Winter Temperature(Fahrenheit)','Crabs(Millions)')
    r = correlationCoe(merged_df,"Winter(Dec-Feb)","Total Number of Crabs in Millions (All Ages)","Total Number of Crabs in Millions vs Mean Winter Temperature In Maryland")
    logger.info(f"Winter: {r}")
    print(r)

    regressionGraph("Spring(Mar-May)","Total Number of Crabs in Millions (All Ages)",merged_df,"Total Number of Crabs in Millions vs Mean Spring Temperature In Maryland",'Mean Spring Temperature(Fahrenheit)','Crabs(Millions)')
    r = correlationCoe(merged_df,"Spring(Mar-May)","Total Number of Crabs in Millions (All Ages)","Total Number of Crabs in Millions vs Mean Spring Temperature In Maryland")
    logger.info(f"Spring: {r}")
    print(r)

    regressionGraph("Summer(Jun-Aug)","Total Number of Crabs in Millions (All Ages)",merged_df,"Total Number of Crabs in Millions vs Mean Summer Temperature In Maryland",'Mean Summer Temperature(Fahrenheit)','Crabs(Millions)')
    r = correlationCoe(merged_df,"Summer(Jun-Aug)","Total Number of Crabs in Millions (All Ages)","Total Number of Crabs in Millions vs Mean Summer Temperature In Maryland")
    logger.info(f"Summer: {r}")
    print(r)

    regressionGraph("Autum(Sep-Nov)","Total Number of Crabs in Millions (All Ages)",merged_df,"Total Number of Crabs in Millions vs Mean Fall Temperature In Maryland",'Mean Fall Temperature(Fahrenheit)','Crabs(Millions)')
    r = correlationCoe(merged_df,"Autum(Sep-Nov)","Total Number of Crabs in Millions (All Ages)","Total Number of Crabs in Millions vs Mean Fall Temperature In Maryland")
    logger.info(f"Autum: {r}")
    print(r)

    #Predict next years crab count based on average 2024 summer and spring temperatures
    pred = predictiveModel("Spring(Mar-May)","Summer(Jun-Aug)",merged_df)
    print(pred)
    logger.info(f"2024 crab prediction: {pred}")
    logger.info('Finished')
    
if __name__ == '__main__':
    main()

























