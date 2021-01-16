import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import math
import matplotlib.pyplot as plt
import datetime 



#---------------------------------------                       -------------------------------
#---------------------------------------                       -------------------------------
# -------------------------------           IMPORT CSV FILES             -------------------------
#---------------------------------------                       -------------------------------
#---------------------------------------                       -------------------------------
#bale sto train_data to arxeio train 
#bale sto feat_data to arxeio features

train_data = pd.read_csv("train.csv")
feat_data = pd.read_csv("features.csv", sep=";")


#elegekse ton typo twn dedomenwn ths kathe sthlhs
print("printing data types")
print(train_data.dtypes) 
print(feat_data.dtypes)



#---------------------------------------                       -------------------------------
#---------------------------------------                       -------------------------------
#--------------------------------------- TREAT MISSING VALUES -------------------------------
#---------------------------------------                       -------------------------------
#---------------------------------------                       -------------------------------




#tsekare an loipoyn kapoies times
print("Checking for missing values")
print(train_data.isnull().sum())
print("Checking for missing values features")
print(feat_data.isnull().sum())


#to unemployment exei missing values
#bazoume ton meso oro sta pedia missing
feat_data['Unemployment'] = feat_data['Unemployment'].fillna(np.mean(feat_data['Unemployment'] ))

#ksana tsekare an exei missing values
print("Checking for missing values features")
print(feat_data.isnull().sum())





#---------------------------------------                       -------------------------------
#---------------------------------------                       -------------------------------
#---------------------------            FIX DIFFERENT DATE FORMATS     -----------------------------
#---------------------------------------                       -------------------------------
#---------------------------------------                       -------------------------------


#Ta arxeia features kai train exoyn diaforetika date formats
#Prepei na einai ta idia gia na ginei swsta to merge
#Metatrepoume ta Date pedia kai twn 2 apo object se datetime64[ns]

#metetrepse to feat_data se datetime object
#to dayfirst=True epeidh xwris ayto to datetime metatrepei tis hmeromhnies sto amerikaniko format 
#enw to test ta exei sto eyrwpaiko format 

feat_data['Date'] = pd.to_datetime(feat_data.Date, dayfirst=True)

#print feat types
print("-----------feat_data--------")
print(feat_data.head())
print(feat_data.dtypes)



#metetrepse to train_data se datetime object
train_data['Date'] = pd.to_datetime(train_data.Date)

print("-----------train_data--------")
print(train_data.head())
print(train_data.dtypes) 




#---------------------------------------                                         -------------------------------
#---------------------------------------                                            -------------------------------
#----------------------------        MERGE train_data + feat_data to all_data     --------------------
#---------------------------------------                                         -------------------------------
#---------------------------------------                                         -------------------------------




print("-----------features and train shape--------")
print(feat_data.shape)
print(train_data.shape)


# Merge feature and training data in all_data
all_data = pd.merge(feat_data, train_data, on = ['Store', 'Date', 'IsHoliday'], how = 'inner')


#Check for missing values in all_data
print("Checking for missing values all_data")
print(all_data.isnull().sum())
print("-----------all_data shape and head(10)---------")
print(all_data.shape)
print(all_data.head(10)) 



#---------------------------------------                                         -------------------------------
#---------------------------------------                                            -------------------------------
#----------------------------        MERGE test + feat_data to test_data     --------------------
#---------------------------------------                                         -------------------------------
#---------------------------------------                                         -------------------------------


#to test_data (train.csv) periexei ~10.000 poy aferesame apo to telos toy train.csv (sort by date)
#gia na sygkrinoume tis problepseis mas me ta dedomena poy exoyme


test = pd.read_csv("test.csv")

print("-------------test_data info---------")
print(test.head())
print(test.dtypes) 
print(test.isnull().sum())


#kane th steilh dates kai toy arxeioy test datetime64[ns] gia ton idio logo poy anaferame parapanw

test['Date'] = pd.to_datetime(test.Date)

print("-----------test head and types--------")
print(test.head())
print(test.dtypes) 



# Merge feature and training data in all_data
test_data = pd.merge(feat_data, test, on = ['Store', 'Date', 'IsHoliday'], how = 'inner')



print("-----Checking for missing values test_data------")
print(test_data.isnull().sum())
print("-----------test_data shape and head(10)---------")
print(test_data.shape)
print(test_data.head(10))





#Set index to the data column
""" data.index = pd.to_datetime(data['Date'])
print (data.head())

#Diegrapse th deyterh sthlh date 
data  = data.drop(['Date'], axis = 1)
print (data.head()) """





#den fainetai na mas leipoun kapoia values
#logika ayto tha allaksei otan kanoyme merge kai to features.csv

#orise tis x,y metablhtes (y ayto poy theloume na problepsoume)



""" plt.plot(x, y, 'x', color='blue', alpha=0.5)
plt.xlabel("Date")
plt.ylabel("Sales")
plt.show()

 """




""" predict = "Weekly_Sales"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
 
print (X)
print("tell me y!")
print (y)

x_train, y_train, x_test, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

print("teell me y!!")
print (y_test) """