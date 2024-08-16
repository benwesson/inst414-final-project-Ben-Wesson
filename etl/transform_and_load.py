
import pandas as pd




def dropCommas (df):
    """
    Remove Commas from numbers in dataframes

    Parameters
    df : pandas dataframe
        dataset on crab populations for a given year for a certain state.
    
    Returns
    df : Datasest with numbers as integers 
    """
    df = df.replace(',','', regex=True)
    return df

def dropColumns (df,list):
    """
    Remove Commas from numbers in dataframes

    Parameters
    df : pandas dataframe
        dataset on crab populations for a given year for a certain state.
    
    Returns
    df : Datasest with numbers as integers 
    """
    
    df.drop(df.columns[list],axis = 1, inplace = True)
    return df


#Make sure data is all ints
def convertData(df1,df2):
    """
    Convet column values to numeric

    Parameters
    df1: pandas dataframe
        Dataset on crab populations for a given year for Maryland. 
    df2: pandas dataframe
         Dataset on seasonal recorded temperatures for a given year for Maryland.
    
    Returns
    df1 : Crab population with all numeric values
    df2 : Temperture dataset with all numeric values
    """
    convert1 = {'Year' : int, 'Total Number of Crabs in Millions (All Ages)' : int}
    convert2 = {'Year': int,  'Annual': float,'Winter(Dec-Feb)': float,'Spring(Mar-May)': float,'Summer(Jun-Aug)': float,'Autum(Sep-Nov)': float,}
    df1 = df1.astype(convert1)
    df2 = df2.astype(convert2)
    return df1,df2



def mergeDf(df1,df2):
    """
    Create merged database with inner join

    Parameters
    df1 : pandas dataframe
        Dataset on crab populations for a given year for Maryland. 
    df2 : pandas dataframe
    Returns
    df : A pandas dataframe consisting of the parameter dataframes
    """
    mergedData = pd.merge(df1,df2,how="inner",on=["Year"])
    return mergedData


