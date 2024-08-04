import extract
import pandas as pd

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

#Call function to drop commas in population numbers
mdComma = dropCommas(md)
ncComma = dropCommas(nc)

#Call function to drop uneeded columns 
mdDrop = dropColumns(mdComma,mdList)
ncDrop = dropColumns(ncComma,ncList)
mdTempDrop = dropColumns(mdTemp,mdTempList)

#Rename column
#mdDrop.rename(columns = {'Survey Year (Year Survey Ended)':'Year'},inplace =True)

#print(mdDrop)

#mdDrop.set_index(['Year'], inplace = True)
#mdTempDrop.set_index(['Year'], inplace = True)

mdTempDrop.drop(mdTempDrop.tail(5).index,inplace=True)
print(mdDrop)
print(mdTempDrop)

#mdDrop['Year'] = mdDrop['Year'].astype(int)
print(mdDrop.columns)
#print(mdDrop.columns)
convert = {'Year' : int, 'Total Number of Crabs in Millions (All Ages)' : int}
mdDrop = mdDrop.astype(convert)
#print(mdDrop.dtypes)
convert = {'Year' : int, 'Annual' : int}
mdTempDrop = mdTempDrop.astype(convert)
#print(mdTempDrop.dtypes)
#mdDrop['Year'] = mdDrop['Year'].astype(int)
#mdTempDrop['Year'] = mdTempDrop['Year'].astype(int)

#Merge databases
mergedData = pd.merge(mdDrop,mdTempDrop,how="inner",on=["Year"])
#print(dftest)
#print(dftest)

#Write cleaned dataframes to new CSVs
mergedData.to_csv('data/cleaned/mergedData.csv',header=True, index=False)

#dftest.to_csv(path_or_buf="data\cleaned")
##mdTempDrop.to_csv('mdTempDrop.csv',header=True, index=False)
#print(mdDrop)
#print(ncDrop)

#Merge dataframes
