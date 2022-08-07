#importing libraries
import pandas as pd
import numpy as np

#helper function, shows all different datatypes in a dataframe
def showDatatypes(dataframe):
    dtypes = []
    for columns in dataframe:
        currentdtype = dataframe[columns].dtypes
        if currentdtype not in dtypes:
            dtypes.append(currentdtype)
    return dtypes
#print(showDatatypes(x))

#function that returns list contaning names of categorical and continous columns
#list[0] is categorical data
#list[1] is continuous data
def columnCategories(categorical_dtypes, continuous_dtypes, dataframe):
    column_categories = [[],[]]
    for columns in dataframe:
        currentdtype = dataframe[columns].dtypes
        if currentdtype in continuous_dtypes:
            column_categories[1].append(columns)
        else:
            column_categories[0].append(columns)
    return column_categories

#function to replace None values with 0 for continuous data
#replace None values with str 'None' for categorical data
def replaceNA(categorical_columns, continuous_columns, dataframe):
    for columns in dataframe:
        if columns in categorical_columns:
            dataframe[columns] = dataframe[columns].fillna('None')
        else:
            dataframe[columns] = dataframe[columns].fillna(0)
    return dataframe
        
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
    if len(columndict)>1:
        return True
    return False

#drop redundant columns: see checkColumnValidity ontop
def dropRedundant(categorical_columns, dataframe):
    dropped_columns = []
    for column in categorical_columns:
        columndata = dataframe[column]
        if checkColumnValidity(createColumnDict(list(columndata))):
            continue
        else:
            dropped_columns.append(column)    
    categorical_columns = [i for i in categorical_columns if i not in dropped_columns]
    dataframe.drop(dropped_columns,axis=1,inplace=True)
    return dataframe

'''

#polynomial regression: r2 score: , rmse:
from sklearn.preprocessing import PolynomialFeatures

pf = PolynomialFeatures(degree=3)
xtrain = pf.fit_transform(xtrain)
poly_regressor = LinearRegression()
poly_regressor.fit(xtrain, ytrain["SalePrice"].values)

#polynomial regression: metrics and predicting values
poly_xtest = pf.transform(xtest)
predictions = poly_regressor.predict(xtest)

print(mean_squared_error(ytest["SalePrice"].values, predictions, squared=False))
print(r2_score(ytest["SalePrice"].values, predictions))

#ensemble learning, RandomForest: r2 score: , rmse:
'''
