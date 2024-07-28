import extract
import pandas as pd

md = extract.marylandDF
nc = extract.northCarolinaDF
mdList = [2,3,4,5,6]
ncList = [1,2,3]

def dropCommas (df):
    df = df.replace(',','', regex=True)
    return df

def dropColumns (df,list):
    df.drop(df.columns[list],axis = 1, inplace = True)
    return df

mdComma = dropCommas(md)
ncComma = dropCommas(nc)

mdDrop = dropColumns(mdComma,mdList)
ncDrop = dropColumns(ncComma,ncList)

mdDrop.to_csv('mdDropped.csv',header=True, index=False)
ncDrop.to_csv('ncDropped.csv',header=True, index=False)

#print(mdDrop)
#print(ncDrop)

