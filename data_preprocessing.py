#importing libraries
import pandas as pd
import numpy as np

#data preprocessing
data = pd.read_csv("train.csv")
x = data.iloc[:,:-1]
y = data.iloc[:,-1]

#helper function, shows all different datatypes in dataframe
def showDatatypes(dataframe):
    dtypes = []
    for columns in dataframe:
        currentdtype = dataframe[columns].dtypes
        if currentdtype not in dtypes:
            dtypes.append(currentdtype)
    return dtypes
#print(showDatatypes(x))

#replace NA in continuous data columns with 0
#replace NA in categorical values with 
categorical_dtypes = ['O']
continuous_dtypes = ['int64','float64']
categorical_columns = []
continuous_columns = []
for columns in x:
    currentdtype = x[columns].dtypes
    if currentdtype in continuous_dtypes:
        x[columns] = x[columns].fillna(value=0)
        continuous_columns.append(columns)
    else:
        x[columns] = x[columns].fillna('None')
        categorical_columns.append(columns)
        
#find redundant columns 
#create dictionary containing unique data and count for each column
def createColumnDict(columndata):
    newdict = {}
    for i in range(len(columndata)):
        if str(columndata[i]) not in newdict:
            newdict[str(columndata[i])]=columndata.count(columndata[i])
    return newdict

#check categorical data if there are enough variety of categories
def checkColumnValidity(columndict):
    if len(columndict)>2:
        return True
    return False

#iterate to find redundant categorical columns
items = x.iteritems()
acceptedcolumns = []
droppedcolumns = []
for label, columndata in items:
    if checkColumnValidity(createColumnDict(list(columndata))):
        acceptedcolumns.append(label)
    else:
        droppedcolumns.append(label)    
    
#dropping redundant columns
x.drop(droppedcolumns,axis=1,inplace=True)
print(x)




#one hot encoding
#from sklearn.preprocessing import OneHotEncoder
#from sklearn.compose import ColumnTransformer
















