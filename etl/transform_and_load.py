
import pandas as pd
"""
#Import the raw dataframes from the extract file. No changes have been made yet
md = extract.marylandDF
nc = extract.northCarolinaDF
mdTemp = extract.mdTempDF

print(md.columns)
#These lists repersent the columns I want to drop in the datasets
mdList = [2,3,4,5,6]
ncList = [1,2,3]
mdTempList = [1,2,3,4,5,6,7,8,9,10,11,12]

#Planned feature
#Add function to create mergerd CSV with shared years
#Convert to common units. 
#Not needed yet because I am at first focusing on measuirng percent change

"""


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
    convert1 = {'Year' : int, 'Total Number of Crabs in Millions (All Ages)' : int}
    convert2 = {'Year': int,  'Annual': float,'Winter(Dec-Feb)': float,'Spring(Mar-May)': float,'Summer(Jun-Aug)': float,'Autum(Sep-Nov)': float,}
    df1 = df1.astype(convert1)
    df2 = df2.astype(convert2)
    return df1,df2

#print(mdDrop.dtypes)

def mergeDf(df1,df2):
    mergedData = pd.merge(df1,df2,how="inner",on=["Year"])
    return mergedData
#print(mdTempDrop.dtypes)

"""
#Merge databases

print(mergedData)

#Write cleaned dataframes to new CSVs
mergedData.to_csv('data/cleaned/mergedData.csv',header=True, index=False)
mdDrop.to_csv('data/cleaned/mdDropped.csv',header=True, index=False)
ncDrop.to_csv('data/cleaned/ncDropped.csv',header=True, index=False)



"""
