#added stuff in car.data cause pandas take first line of a data file as attributes name
#eg Student name , class etc
#so u cant just have david,sf1804... etc
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model , preprocessing
from sklearn.preprocessing import OneHotEncoder
import pickle
from IPython.display import display
import sys
import datetime
from datetime import datetime as dt
import dateutil.parser
import matplotlib.pyplot as plt
import seaborn as sns
import pylab
from sklearn.metrics import average_precision_score

from matplotlib import style

data = pd.read_csv("dataset_000.csv")
print(data.dtypes)


data['SERVER'] = data['SERVER'].astype(str)
#pd.set_option('display.max_rows', 1800)
#pd.set_option('display.max_colwidth', -1)

#data['newColumn'] = 'nginx/1.10.1'
#data['SERVER'] = data['newColumn']
#pd.to_numeric(data['SERVER'], errors='coerce')

print(data['SERVER'])
#print(data.dtypes)
#Very useful , can see data types

#data['SERVER'].fillna(-1, inplace=True)

le = preprocessing.LabelEncoder()
data = data.apply(le.fit_transform)

#data['CONTENT_LENGTH_NONE'] =  'No'
# data['CONTENT_LENGTH'].replace('NaN','-1',inplace=True)
# data.loc[data['CONTENT_LENGTH'] == 'None' , 'CONTENT_LENGTH'] = '-1'
#data['CONTENT_LENGTH'].isnull().values.any()

data['CONTENT_LENGTH'].fillna(-1, inplace=True)

j = 0
if [data['CONTENT_LENGTH'].isnull().values.any()]:
    j = j + 1
    print("number of nans is ",j)
else:
    print("dont have la")
#1)Replace it with -1 , -2 , 0 etc
#2)Use the mean of everyth , or median
#Note that both 1) and 2) can be tested with and without the content_length_none

#Plot graphs of time in a better manner
#Watch vid of chrome ext to see what is feasible to implement at this point

print("Data for content length none" ,data['CONTENT_LENGTH'])
#data['CONTENT_LENGTH'] = data['CONTENT_LENGTH'].map({'NA': -
# print("Malicious :",j)
# print("Benign :",k)
# Malicious : 216 - 12.13%
# Benign : 1565 - 0.88%
# Total 1781 

le = preprocessing.LabelEncoder()
#WHOIS statepro and WHOIS country
#ALOT none values
data = data[data.WHOIS_REGDATE != 'None']
data = data[data.WHOIS_REGDATE != '2002-03-20T23:59:59.0Z']
data = data[data.WHOIS_REGDATE != 'b']
data = data[data.WHOIS_REGDATE != '0']



data = data[data.WHOIS_UPDATED_DATE != 'None']

data['WHOIS_REGDATE'] = pd.to_datetime(data.WHOIS_REGDATE,format='%d/%m/%Y %H:%M')

data['WHOIS_UPDATED_DATE'] = pd.to_datetime(data.WHOIS_UPDATED_DATE,format='%d/%m/%Y %H:%M')

data['DATE_DIFF'] = data['WHOIS_UPDATED_DATE'] - data['WHOIS_REGDATE']
#data.loc[data['DATE_DIFF'] < 0 , 'DATE_DIFF'] = '1/1/1900 00:00'

# print(data['WHOIS_UPDATED_DATE'].head(5))
# print(data['WHOIS_REGDATE'].head(5))
# print(data['DATE_DIFF'].head(5))
data['WHOIS_REGDATE_TRY'] = data['WHOIS_REGDATE'] 
data['DATE_DIFF_TRY'] = data['DATE_DIFF'] 

data['WHOIS_UPDATED_DATE_TRY'] = data['WHOIS_UPDATED_DATE'] 
data = data.set_index('DATE_DIFF_TRY')

#data = data.set_index('WHOIS_REGDATE')


# Add columns with year, month, and weekday name
# data['Year'] = data.index.year
# data['Month'] = data.index.month
# print(data['Month'].head(5))
# data['Weekday Name'] = data.index.weekday_name
# Display a random sampling of 5 rows
# data.sample(5, random_state=0)
sns.set(rc={'figure.figsize':(11, 4)})
#smth = data['Type'].plot(linewidth=0.5,kind='scatter',style='.')

data['DATE_DIFF'].plot(style='.')

#pylab.show()

#print(data['WHOIS_COUNTRY'].loc[data.WHOIS_COUNTRY == 'None'])


#Removing rows with value such as 'None' , 'b' etc
#create new column to store the none first

#data['WHOIS_REGDATE_NONE'] = data['WHOIS_REGDATE'].loc[data.WHOIS_REGDATE == 'X']
#print(data['WHOIS_REGDATE_NONE'])
#data['WHOIS_UPDATED_DATE_NONE'] = data['WHOIS_UPDATED_DATE'].loc[data.WHOIS_UPDATED_DATE == 'None']

#Theres 21 "None" column
data = data[data.WHOIS_REGDATE != 'None']
data = data[data.WHOIS_REGDATE != 'b']
data = data[data.WHOIS_REGDATE != '2002-03-20T23:59:59.0Z']
data = data[data.WHOIS_REGDATE != '0']

data = data[data.WHOIS_UPDATED_DATE != 'None']


#dummy_df_dates = pd.DataFrame({'age': ['0-20', '20-40', '40-60','60-80']})




#Previous data : 7/10/1997 4:00 , of type Object -> String
#print(type(data['WHOIS_REGDATE']))
# print(data['WHOIS_REGDATE'].head())
# print("After formaatting ==")
data['WHOIS_REGDATE'] = pd.to_datetime(data.WHOIS_REGDATE,format='%d/%m/%Y %H:%M')
# print(data['WHOIS_REGDATE'].head())

#After formmating : 1997-10-07 04:00:00 , of type Object -> datetime64[ns]
#print(type(data['WHOIS_REGDATE']))
#print(data['WHOIS_REGDATE'].head())

data['WHOIS_UPDATED_DATE'] = pd.to_datetime(data.WHOIS_UPDATED_DATE,format='%d/%m/%Y %H:%M')

#20 years ago (Timestamp 20)

ts20 = datetime.datetime.today() - datetime.timedelta(days=20*365) #very old
ts15 = datetime.datetime.today() - datetime.timedelta(days=15*365) #very old

ts10 = datetime.datetime.today() - datetime.timedelta(days=10*365) #old
ts3 = datetime.datetime.today() - datetime.timedelta(days=3*365) #new
ts1 = datetime.datetime.today() - datetime.timedelta(days=365) #very new
ts0 = datetime.datetime.today() - datetime.timedelta(days=7) #newest
tsnow = datetime.datetime.today()

# print("ten years ago")
# print(data['WHOIS_REGDATE'].loc[data.WHOIS_REGDATE <= ts20]) #20 years old or older
# print(data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts10) & (data.WHOIS_REGDATE > ts20)]) #less than 20 y/o ,older or equal to 10
# print(data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts3) & (data.WHOIS_REGDATE > ts10)])
# print(data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts1) & (data.WHOIS_REGDATE > ts3)])
# print(data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts0) & (data.WHOIS_REGDATE > ts1)]) #past 7 day




# date20 = data['WHOIS_REGDATE'].loc[data.WHOIS_REGDATE <= ts20]
# date10 = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts10) & (data.WHOIS_REGDATE > ts20)]
# date3 = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts3) & (data.WHOIS_REGDATE > ts10)]
# date1 =  data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts1) & (data.WHOIS_REGDATE > ts3)]
# date0 =  data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts0) & (data.WHOIS_REGDATE > ts1)]
# dateRemain = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= tsnow) & (data.WHOIS_REGDATE > ts0)]

# data['veryOld'] = data['WHOIS_REGDATE'].loc[data.WHOIS_REGDATE <= ts20 ]
# data['old'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts10) & (data.WHOIS_REGDATE > ts20)]
# data['new'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts3) & (data.WHOIS_REGDATE > ts10)]
# data['veryNew'] =  data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts1) & (data.WHOIS_REGDATE > ts3)]
# data['newest'] =  data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts0) & (data.WHOIS_REGDATE > ts1)]
# data['remainingREGDATE'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= tsnow) & (data.WHOIS_REGDATE > ts0)]
data['WHOIS_DATE_DIFF'] =  ""




data['WHOIS_REGDATE_FORMATTED'] = ""
data.loc[data['WHOIS_REGDATE'] <= ts15 , 'WHOIS_REGDATE_FORMATTED'] = 'VeryOld'
data.loc[(data['WHOIS_REGDATE'] <= ts3) & (data['WHOIS_REGDATE'] > ts15), 'WHOIS_REGDATE_FORMATTED'] = 'Old'
data.loc[(data['WHOIS_REGDATE'] <= ts1) & (data['WHOIS_REGDATE'] > ts3), 'WHOIS_REGDATE_FORMATTED'] = 'New'
data.loc[(data['WHOIS_REGDATE'] <= tsnow) & (data['WHOIS_REGDATE'] > ts1), 'WHOIS_REGDATE_FORMATTED'] = 'VeryNew'

# print(data['WHOIS_REGDATE_FORMATTED'])
#Solve server issue
data['SERVER'] = pd.to_numeric(data['SERVER'], errors='coerce')
print(len(data['SERVER']))

data= data.apply(le.fit_transform)

# p = 'WHOIS_REGDATE_FORMATTED'
# style.use("ggplot")
# pyplot.bar(data[p],data["Type"])
# pyplot.xlabel(p)
# pyplot.ylabel("Type")
# pyplot.show()    

#df.loc[df['First Season'] > 1990, 'First Season'] = 1


# data['WHOIS_REGDATE'] = np.where(data['WHOIS_REGDATE'] == data['veryOld'] , 'veryOld')
# print(data['WHOIS_REGDATE'])

# data[data.WHOIS_REGDATE == (data.WHOIS_REGDATE <= ts10)] = "veryOld"
# print(data[data.WHOIS_REGDATE == (data.WHOIS_REGDATE <= ts10)])
# data[data.WHOIS_REGDATE == (data.WHOIS_REGDATE <= ts20)] = "old"
# data[data.WHOIS_REGDATE == (data.WHOIS_REGDATE <= ts20)] = "new"
# data[data.WHOIS_REGDATE == (data.WHOIS_REGDATE <= ts20)] = "veryNew"
# data[data.WHOIS_REGDATE == (data.WHOIS_REGDATE <= ts20)] = "newest"
# data[data.WHOIS_REGDATE == (data.WHOIS_REGDATE <= ts20)] = "remainingREGDATE"
# print("ABOVE HERE")
# date20 = "veryOld"
# date10 = "old"
# date3 = "new"
# date1 = "veryNew"
# date0 = "newest"
# dateRemain = "remainingREGDATE"



# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].map(date20,"veryOld")
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].map(date10,"old")
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].map(date3,"new")
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].map(date1,"veryNew")
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].map(date0,"newest")
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].map(dateRemain,"remainingREGDATE")

# print(data['WHOIS_REGDATE'])

#print(data['WHOIS_REGDATE'].head())

#data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].replace([data.WHOIS_REGDATE <= ts20],"oldest" ,inplace=True)

# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].loc[data.WHOIS_REGDATE <= ts20].replace(data['WHOIS_REGDATE'],"oldest" ,inplace=True)
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts10) & (data.WHOIS_REGDATE > ts20)].replace(data['WHOIS_REGDATE'],"very old",inplace=True)
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts3) & (data.WHOIS_REGDATE > ts10)].replace(data['WHOIS_REGDATE'],"old",inplace=True)
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts1) & (data.WHOIS_REGDATE > ts3)].replace(data['WHOIS_REGDATE'],"new",inplace=True)
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= ts0) & (data.WHOIS_REGDATE > ts1)].replace(data['WHOIS_REGDATE'],"very new",inplace=True)
# data['WHOIS_REGDATE'] = data['WHOIS_REGDATE'].loc[(data.WHOIS_REGDATE <= tsnow) & (data.WHOIS_REGDATE > ts0)].replace(data['WHOIS_REGDATE'],"newest",inplace=True)



# if (data['WHOIS_REGDATE'] <= ts20):
#     data['WHOIS_REGDATE'].replace(data['WHOIS_REGDATE'],"oldest")
# elif ( (data['WHOIS_REGDATE'] <= ts10) & (data['WHOIS_REGDATE'] > ts20) ):
#     data['WHOIS_REGDATE'].replace(data['WHOIS_REGDATE'],"very old")
# elif ( (data['WHOIS_REGDATE'] <= ts3) & (data['WHOIS_REGDATE'] > ts10) ):
#     data['WHOIS_REGDATE'].replace(data['WHOIS_REGDATE'],"old")
# elif ( (data['WHOIS_REGDATE'] <= ts1) & (data['WHOIS_REGDATE'] > ts3) ):
#     data['WHOIS_REGDATE'].replace(data['WHOIS_REGDATE'],"new")
# elif ( (data['WHOIS_REGDATE'] <= ts0) & (data['WHOIS_REGDATE'] > ts1) ):
#     data['WHOIS_REGDATE'].replace(data['WHOIS_REGDATE'],"very new")
# elif ( (data['WHOIS_REGDATE'] <= tsnow) & (data['WHOIS_REGDATE'] > ts0) ):
#     data['WHOIS_REGDATE'].replace(data['WHOIS_REGDATE'],"newest")

#print(model.predict(

