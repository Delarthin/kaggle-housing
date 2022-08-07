import pandas as pd
import data_preprocessing as dataPreprocessing
data = pd.read_csv("csv_files/train.csv")
x = data.iloc[:,:-1]
y = data.iloc[:,-1].to_frame()

#remove ID column from x, insert at column 0 for y
y.insert(loc=0, column='Id', value=[i for i in x["Id"]])
x = x.drop(labels='Id',axis=1,inplace=False)

#check datatypes, manually separate them into categorical vs continuous
#print(dataPreprocessing.showDatatypes)
categorical_dtypes = ['O']
continuous_dtypes = ['int64','float64']

#get labels of categorical and continuous columns
columncategories = dataPreprocessing.columnCategories(categorical_dtypes, continuous_dtypes, x)
categorical_columns = columncategories[0]
continuous_columns = columncategories[1]

#replace NA values
x = dataPreprocessing.replaceNA(categorical_columns, continuous_columns, x)

#find and drop redundant columns
x = dataPreprocessing.dropRedundant(categorical_columns, x)

#train test split
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size=0.2,random_state=0)

#scale data
#standard scaling for continuous
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
ss = StandardScaler()
xtrain[continuous_columns] = ss.fit_transform(xtrain[continuous_columns])

#OHE for categorical
ct = ColumnTransformer([("ohe",OneHotEncoder(handle_unknown="ignore"),categorical_columns)],remainder="passthrough")
xtrain = ct.fit_transform(xtrain)

#transform to poly features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3)
xtrain = poly.fit_transform(xtrain)

#Polynomial Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(xtrain,ytrain["SalePrice"].values)

#Polynomial Regression: metrics and predicting values
from sklearn.metrics import mean_squared_error, r2_score
xtest[continuous_columns] = ss.transform(xtest[continuous_columns])
xtest = ct.transform(xtest)
xtest = poly.transform(xtest)
predictions = regressor.predict(xtest)
print(mean_squared_error(ytest["SalePrice"].values, predictions, squared=False))
print(r2_score(ytest["SalePrice"].values, predictions))

