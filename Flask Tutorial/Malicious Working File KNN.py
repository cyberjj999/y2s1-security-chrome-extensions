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
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import classification_report
from sklearn.metrics import average_precision_score
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import roc_curve, precision_recall_curve, auc, make_scorer, recall_score, accuracy_score, precision_score, confusion_matrix , roc_auc_score
from inspect import signature
import pylab
from collections import defaultdict


data = pd.read_csv("dataset_000.csv")

#print(data.isnull().sum()) #show nubmer of null values in ur dataframe
#Removing rows with value such as 'None' , 'b' etc
#create new column to store the none first

#Create 2 new columns to store my my categorized data
#But since i need to do comparison of time , to group them , i have to convert the data to datetime obj
#Having none in some of the rows will cause error
#To resolve this , I create a abitrary date , eg 1/1/1900 , to store my NONES
#Then i set a condition , those before 500 years ago , would be replaced to none
#This actually resolve the problem of datetime obj

#Create imputer object to deal with NaN values in numerical columns 
#imputer = Imputer(missing_values='NaN',strategy='mean',axis=0)
#imputer.fit_transform(data['URL_LENGTH','NUMBER_OF_SPECIAL_CHARACTERS])

data['WHOIS_REGDATE_FORMATTED'] = ""
data['WHOIS_UPDATE_FORMATTED'] = ""
#Convert nones into abitrary date 1900
data.loc[data['WHOIS_UPDATED_DATE'] == 'None' , 'WHOIS_UPDATED_DATE'] = '1/1/1900 00:00'
data.loc[data['WHOIS_REGDATE'] == 'None' , 'WHOIS_REGDATE'] = '1/1/1900 00:00'

# data.loc[data['WHOIS_REGDATE'] == '15/2/2003 19:10' , 'WHOIS_REGDATE'] = '1/1/1900 00:00'
# data.loc[data['WHOIS_REGDATE'] == '2/7/2019 15:52' , 'WHOIS_REGDATE'] = '1/1/1900 00:00'


data['CONTENT_LENGTH_NONE'] = 'No'

data['CONTENT_LENGTH'].fillna(-1, inplace=True)
data.loc[data['CONTENT_LENGTH'] == -1 , 'CONTENT_LENGTH_NONE'] = 'Yes'
# data.loc[data['CONTENT_LENGTH_NONE'] == -1 , 'CONTENT_LENGTH_NONE'] = 'Yes'
# data.loc[data['CONTENT_LENGTH_NONE'] != -1 , 'CONTENT_LENGTH_NONE'] = 'No'

#print(data['CONTENT_LENGTH_NONE'])

#1)Replace it with -1 , -2 , 0 etc
#2)Use the mean of everyth , or median
#Note that both 1) and 2) can be tested with and without the content_length_none

#Plot graphs of time in a better manner
#Watch vid of chrome ext to see what is feasible to implement at this point


#Theres 21 "None" column
#data = data[data.WHOIS_REGDATE != 'None']
data = data[data.WHOIS_REGDATE != 'b']
data = data[data.WHOIS_REGDATE != '2002-03-20T23:59:59.0Z']
data = data[data.WHOIS_REGDATE != '0']

#Make everything uppercase
data['CHARSET'] = data['CHARSET'].str.upper()
data['SERVER'] = data['SERVER'].str.upper() 
data['WHOIS_COUNTRY'] = data['WHOIS_COUNTRY'].str.upper() 
data['WHOIS_STATEPRO'] = data['WHOIS_STATEPRO'].str.upper() 



#data = data[data.WHOIS_UPDATED_DATE != 'None']


#Convert to datetime object
data['WHOIS_REGDATE'] = pd.to_datetime(data.WHOIS_REGDATE,format='%d/%m/%Y %H:%M')

#After formmating : 1997-10-07 04:00:00 , of type Object -> datetime64[ns]
#print(type(data['WHOIS_REGDATE']))
#print(data['WHOIS_REGDATE'].head())

data['WHOIS_UPDATED_DATE'] = pd.to_datetime(data.WHOIS_UPDATED_DATE,format='%d/%m/%Y %H:%M')

#15 years ago (Timestamp 15)
referenceDate = dt.strptime('01/01/2018','%d/%m/%Y')
#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')


noneFormatter = referenceDate - datetime.timedelta(days=100*365) #very old

ts15 = referenceDate - datetime.timedelta(days=15*365) #very old
ts10 = referenceDate - datetime.timedelta(days=10*365) #old
ts5 = referenceDate - datetime.timedelta(days=5*365) #old
ts3 = referenceDate - datetime.timedelta(days=3*365) #new
ts1 = referenceDate - datetime.timedelta(days=365) #very new
ts0 = referenceDate - datetime.timedelta(days=30) #newest


#Replace date with diff string category , based on how long ago it is
#data['WHOIS_REGDATE_FORMATTED'] = "" 

data.loc[data['WHOIS_REGDATE'] <= noneFormatter , 'WHOIS_REGDATE_FORMATTED'] = 'None' #10 years ago (prolly solid)
data.loc[(data['WHOIS_REGDATE'] <= ts10) & (data['WHOIS_REGDATE'] > noneFormatter), 'WHOIS_REGDATE_FORMATTED'] = 'VeryOld' #10 years ago (prolly solid)
data.loc[(data['WHOIS_REGDATE'] <= ts1) & (data['WHOIS_REGDATE'] > ts10), 'WHOIS_REGDATE_FORMATTED'] = 'Old' #1 - 10 yrs
data.loc[(data['WHOIS_REGDATE'] <= ts0) & (data['WHOIS_REGDATE'] > ts1), 'WHOIS_REGDATE_FORMATTED'] = 'New' #30 days to 1 year , alright
data.loc[(data['WHOIS_REGDATE'] <= referenceDate) & (data['WHOIS_REGDATE'] > ts0), 'WHOIS_REGDATE_FORMATTED'] = 'VeryNew' #now to 30 days

data.loc[data['WHOIS_UPDATED_DATE'] <= noneFormatter , 'WHOIS_UPDATE_FORMATTED'] = 'None' #10 years ago (prolly solid)
data.loc[(data['WHOIS_UPDATED_DATE'] <= ts5) & (data['WHOIS_UPDATED_DATE'] > noneFormatter), 'WHOIS_UPDATE_FORMATTED'] = 'VeryOld' #10 years ago (prolly solid)
data.loc[(data['WHOIS_UPDATED_DATE'] <= ts1) & (data['WHOIS_UPDATED_DATE'] > ts5), 'WHOIS_UPDATE_FORMATTED'] = 'Old'
data.loc[(data['WHOIS_UPDATED_DATE'] <= ts0) & (data['WHOIS_UPDATED_DATE'] > ts1), 'WHOIS_UPDATE_FORMATTED'] = 'New'
data.loc[(data['WHOIS_UPDATED_DATE'] <= referenceDate) & (data['WHOIS_UPDATED_DATE'] > ts0), 'WHOIS_UPDATE_FORMATTED'] = 'VeryNew'

#Change server to string type
#data['SERVER'] = data['SERVER'].astype(str)
data['SERVER'].fillna('Others', inplace=True)


# data['CHARSET'] = data['CHARSET'].astype(str)
# data['WHOIS_COUNTRY'] = data['WHOIS_COUNTRY'].astype(str)
# data['WHOIS_STATEPRO'] = data['WHOIS_STATEPRO'].astype(str)
# data['WHOIS_REGDATE_FORMATTED'] = data['WHOIS_REGDATE_FORMATTED'].astype(str)
# data['WHOIS_UPDATE_FORMATTED'] = data['WHOIS_UPDATE_FORMATTED'].astype(str)
# data['CONTENT_LENGTH_NONE'] = data['CONTENT_LENGTH_NONE'].astype(str)
# data['Type'] = data['Type'].astype(int)

#datale = datale.apply(le.fit_transform)
# print(data.head()) 
# data = data.drop(['URL'],axis=1) #DROP columns in pandas
# print(data.head())
le = preprocessing.LabelEncoder()
# le = defaultdict(preprocessing.LabelEncoder)
# temp = data #Store temporaily

# myLabelEncoder = preprocessing.LabelEncoder()

# #URL_LENGTH,NUMBER_SPECIAL_CHARACTERS,CONTENT_LENGTH

# data = data.drop(['URL_LENGTH'],axis=1)
# data = data.drop(['NUMBER_SPECIAL_CHARACTERS'],axis=1)
# data = data.drop(['CONTENT_LENGTH'],axis=1)

# #Dropping stuff i not using
# data = data.drop(['URL'],axis=1)
# data = data.drop(['WHOIS_REGDATE'],axis=1)
# data = data.drop(['WHOIS_UPDATED_DATE'],axis=1)


# myLabelEncoder.fit(data['CHARSET'])
# myLabelEncoder.fit(data['SERVER'])
# myLabelEncoder.fit(data['WHOIS_COUNTRY'])
# myLabelEncoder.fit(data['WHOIS_STATEPRO'])
# myLabelEncoder.fit(data['WHOIS_UPDATE_FORMATTED'])
# myLabelEncoder.fit(data['WHOIS_REGDATE_FORMATTED'])
# myLabelEncoder.fit(data['CONTENT_LENGTH_NONE'])
# np.save('preprocessingObjects/classes.npy', myLabelEncoder.classes_)
# myLabelEncoder = preprocessing.LabelEncoder()
# myLabelEncoder.classes_ = np.load('classes.npy' ,allow_pickle=True)
# print(myLabelEncoder.classes_)
# data = data.apply(myLabelEncoder.transform)

# data = data.apply(lambda x: le[x.name].fit_transform(x))
# print(le.__class__)
# joblib.dump(le,"labelEncoder.sav")
data['CONTENT_LENGTH'] = data['CONTENT_LENGTH'].astype(float)

# print(data.dtypes)

datale = data
# datale['URL_LENGTH'] = temp['URL_LENGTH']
# datale['NUMBER_SPECIAL_CHARACTERS'] = temp['NUMBER_SPECIAL_CHARACTERS']
# datale['CONTENT_LENGTH'] = temp['CONTENT_LENGTH']
#CONFIRMED that the 3 numerical columns are UNTOUCHED

# pd.set_option('display.max_columns', 500)
# print(data.head())

# data = data.apply(le.fit_transform)
#print(data.isnull().sum()) 
# print(datale.head())

# print(datale.head())

#print(datale['SERVER'])
#Deal with SERVER data issue
#datale['SERVER'] = pd.to_numeric(datale['SERVER'], errors='coerce')
#print("Data at this point is " , datale)
#datale = datale.apply(le.fit_transform)


#here
# all_values = data.values.ravel() #convert the dataframe to one long array
# print(all_values)
# le.fit(all_values)
# print(le.classes_)
# joblib.dump(le,"labelEncoder.pkl")
# datale = data

# print(datale['CONTENT_LENGTH'])

# print(datale.head())
# datale['URL_LENGTH'] = temp['URL_LENGTH']
# datale['NUMBER_SPECIAL_CHARACTERS'] = temp['NUMBER_SPECIAL_CHARACTERS']
# datale['CONTENT_LENGTH'] = temp['CONTENT_LENGTH']

#to here

myLeCHARSET = preprocessing.LabelEncoder()
myLeSERVER = preprocessing.LabelEncoder()
myLeCOUNTRY = preprocessing.LabelEncoder()
myLeSTATEPRO = preprocessing.LabelEncoder()
myLeUPDATE = preprocessing.LabelEncoder()
myLeREGDATE = preprocessing.LabelEncoder()
myLeCONTENTL_NONE = preprocessing.LabelEncoder()


datale['CHARSET'] = myLeCHARSET.fit_transform(datale['CHARSET'])
joblib.dump(myLeCHARSET,"preprocessingObjects/myLeCHARSET.pkl")

datale['SERVER'] = myLeSERVER.fit_transform(datale['SERVER'])
joblib.dump(myLeSERVER,"preprocessingObjects/myLeSERVER.pkl")

datale['WHOIS_COUNTRY'] = myLeCOUNTRY.fit_transform(datale['WHOIS_COUNTRY'])
joblib.dump(myLeCOUNTRY,"preprocessingObjects/myLeCOUNTRY.pkl")

datale['WHOIS_STATEPRO'] = myLeSTATEPRO.fit_transform(datale['WHOIS_STATEPRO'])
joblib.dump(myLeSTATEPRO,"preprocessingObjects/myLeSTATEPRO.pkl")

datale['WHOIS_UPDATE_FORMATTED'] = myLeUPDATE.fit_transform(datale['WHOIS_UPDATE_FORMATTED'])
joblib.dump(myLeUPDATE,"preprocessingObjects/myLeUPDATE.pkl")

datale['WHOIS_REGDATE_FORMATTED'] = myLeREGDATE.fit_transform(datale['WHOIS_REGDATE_FORMATTED'])
joblib.dump(myLeREGDATE,"preprocessingObjects/myLeREGDATE.pkl")
#print('im printing whois reg date ' , myLeREGDATE.classes_)

datale['CONTENT_LENGTH_NONE'] = myLeCONTENTL_NONE.fit_transform(datale['CONTENT_LENGTH_NONE'])
joblib.dump(myLeCONTENTL_NONE,"preprocessingObjects/myLeCONTENTL_NONE.pkl")


# print("My label encoder")
# print("=================")
# print("myLeCHARSET : " , myLeCHARSET.classes_)
# print("myLeSERVER : " , myLeSERVER.classes_)
# print("myLeCOUNTRY : " , myLeCOUNTRY.classes_)
# print("myLeSTATEPRO : " , myLeSTATEPRO.classes_)
# print("myLeUPDATE : " , myLeUPDATE.classes_)
# print("myLeREGDATE : " , myLeREGDATE.classes_)
# print("myLeCONTENTL_NONE : " , myLeCONTENTL_NONE.classes_)
# print("=================")

# 3 things i DO not need to label encode
#URL_LENGTH,NUMBER_SPECIAL_CHARACTERS,CONTENT_LENGTH

#pd.set_option('display.max_rows', 100000)

X = datale[["URL_LENGTH","NUMBER_SPECIAL_CHARACTERS","CHARSET","SERVER","CONTENT_LENGTH","CONTENT_LENGTH_NONE","WHOIS_COUNTRY","WHOIS_STATEPRO","WHOIS_REGDATE_FORMATTED","WHOIS_UPDATE_FORMATTED"]].values
print("some of my X value " ,X)

sampleData = [[23,6,4,215,-1,1,43,4,2,2]]

Y = datale['Type']
#Y = datale.Type
ohe = OneHotEncoder(categorical_features=[2,3,5,6,7,8,9],handle_unknown='ignore')

#ohe = OneHotEncoder(categorical_features=[9],handle_unknown='ignore')
X = ohe.fit_transform(X).toarray()

# print("================")
# print("My OHE active feature " , ohe.active_features_)
# print("================")

sampleData = ohe.transform(sampleData).toarray()
# print("My sample data after OHE is " , sampleData)


joblib.dump(ohe,"preprocessingObjects/OHEncoder.pkl")
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y,random_state=10)
# x_train is the training data set.
# y_train is the set of labels to all the data in x_train.

# x_test is the test data set.
# y_test is the set of labels to all the data in x_test.
#print("Before scaling" , datale['CONTENT_LENGTH'])
# print(x_train)

#Scaling done here
sc_X = preprocessing.StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)
joblib.dump(sc_X,"preprocessingObjects/scaler.pkl")

sampleData = sc_X.transform(sampleData.reshape(1, -1))

# y_scaler = preprocessing.StandardScaler()
# y_train = y_scaler.fit_transform(y_train[:, None])[:, 0]
# y_test = y_scaler.transform(y_test[:, None])[:, 0]

# std_scale = preprocessing.StandardScaler().fit(x_train[['URL_LENGTH', 'NUMBER_SPECIAL_CHARACTERS','CONTENT_LENGTH']])
# datale_std = std_scale.fit_transform(x_train[['URL_LENGTH', 'NUMBER_SPECIAL_CHARACTERS','CONTENT_LENGTH']])

# print("After scaling",datale_std)
#The issue is i am only fitting PART of the train data

model = svm.SVC(probability=True,gamma='scale',kernel="linear")
#svm.SVC(probability=True)
model.fit(x_train,y_train)
with open("MaliciousLinkModel.pickle", "wb") as f:
             pickle.dump(model, f)
#              joblib.dump(model, 'saved_model.pkl') 

# joblib.dump(model, 'saved_model.pkl') 

#train_test_split

#testign here
#The issue of same probability can be due to couple of reasons
#1) The way i load the encoders
#2) The way i load the pickle file
#3) The way i encode in the flask server
samplePredictProba = model.predict_proba(sampleData)
print("the sample data prediction is " , samplePredictProba)

#the sample data prediction is  [[9.9999990e-01 1.0000001e-07]]
# # uncomment this to train it in a loop later
# # best = 0
# # for _ in range(2):
# #     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y,test_size = 0.1)


# #     model = svm.SVC()
# #     model.fit(x_train,y_train)
# #     y_pred = model.predict(x_test)
# #     y_score = model.decision_function(x_test)
# #     average_precision = average_precision_score(y_test, y_score)
# #     if average_precision > best:
# #         best = average_precision
# #         with open("MaliciousLinkModel.pickle", "wb") as f:
# #             pickle.dump(model, f)
# # model = KNeighborsClassifier(n_neighbors=7)
# # #takes in 1 parameter , number of neighbours
# # #make sure its odd number and not too big else will have prob

# # model.fit(x_train,y_train)

# '''
# model = svm.SVC()
# model.fit(x_train,y-train)
# y_pred = model.predict(x_test)
# '''

# #acc = model.score(x_test,y_test)
# #print(acc)

# # if acc > best:
# #     best = acc
# #     with open("MaliciousLinkModel.pickle", "wb") as f:
# #         pickle.dump(model, f)


# ohe = joblib.load("encoder.pkl")
# X = ohe.transform(x_test).toarray()

# pickle_in = open("MaliciousLinkModel.pickle" , "rb")
# #opening the model u saved
# model = pickle.load(pickle_in)
# #To load our model into the var model
# # acc = model.score(x_test,y_test)
# # print(acc)
# # models = []
# # models.append(('KNN'))

#SCORING ARE PRINTED HERE
# np.set_printoptions(edgeitems=25)

# print(x_test)
model_probs = model.predict_proba(x_test)
y_pred = model.predict(x_test)
y_score = model.decision_function(x_test)
average_precision = average_precision_score(y_test, y_score)
print('Average precision-recall score: {0:0.2f}'.format(
      average_precision))
# # Of the url classified as Malicious , how many are ACTUALLY malicious?
# # Arnd 0.7 to 0.8 , 75% of the url they say malicious is really malicious
# roc_curve_prob = roc_auc_score(y_test,y_score)       
# print('ROC Curve score: {0:0.2f}'.format(
#       roc_curve_prob))

# # print('=========')
# # print('y_train class distribution')
# # print(y_train.value_counts(normalize=True))
# # print('y_test class distribution')
# # print(y_test.value_counts(normalize=True))
# #About 0.75ish for a low false positive rate

# #First index is chances of it being 0 , 2nd is chances of it being 1
# # [0.94631426 0.05368574]
# # So chances of it being bad is 0.94 , being good is 0.05
# #print("model probability is ",model_probs)
# print("recall score is ", recall_score(y_test,y_pred))
# #Currently recall is 0.46 , meaning it classifies 

print(confusion_matrix(y_test, y_pred))
# #[[384   6]
# # [ 37  17]]
# #False negavtive btm left false positive btm right , top left is tp , btm right is tn

# #For binary classification, sklearn.metrics.f1_score will by default make the assumption that 
# #1 is the positive class, and 0 is the negative class

# # c =  model_probs.flatten() -> change from 2d array to 1d
# # print("After reshaping " , c.shape)
# # Not really shape issue , but forgot to .predict_proba(x_test)[:,1]
# # this takes only the prob of it being positive
# # if u dont define [:,1] , means u get both positive and negative , like 0.7,0.3
# # you shud need the probability of it happening only , so just take the first value


precision_lr , recall_lr , thresholds_lr = precision_recall_curve(y_test,model.predict_proba(x_test)[:,1])
# print("Precision_LR is " ,precision_lr)
# print("Recall_LR is " ,recall_lr)
# print("Thresholds_LR is " ,thresholds_lr)


fig, ax = plt.subplots(figsize=(8,5))
ax.plot(thresholds_lr,recall_lr[1:],label ='Recall')
ax.plot(thresholds_lr,precision_lr[1:],label ='Precision')

ax.set_xlabel("Classification Threshold")
ax.set_ylabel("Precision, Recall")
ax.set_title("SVM Classifier: Precision-Recall")
ax.hlines(y=0.6,xmin=0,xmax=1 ,color = 'red')
ax.legend()
ax.grid()
plt.show()
pylab.show()

print("=========")
y_pred_proba = model.predict_proba(x_test)[:,1]
y_pred_test = (y_pred_proba >= 0.2).astype('int')
CM = confusion_matrix(y_test,y_pred_test)
print("Recall: ", recall_score(y_test,y_pred_test))
print("Precision: ", precision_score(y_test,y_pred_test))
print(CM)



# # Recall-Precision curve here - Uncomment to show
# # precision, recall, _ = precision_recall_curve(y_test, y_score)
# # step_kwargs = ({'step': 'post'}
# #                if 'step' in signature(plt.fill_between).parameters
# #                else {})
# # plt.step(recall, precision, color='b', alpha=0.2,
# #          where='post')
# # plt.fill_between(recall, precision, alpha=0.2, color='b', **step_kwargs)

# # plt.xlabel('Recall')
# # plt.ylabel('Precision')
# # plt.ylim([0.0, 1.05])
# # plt.xlim([0.0, 1.0])
# # plt.title('2-class Precision-Recall curve: AP={0:0.2f}'.format(
# #           average_precision))

# # plt.show()
# # pylab.show()



# #Average precision-recall score: 0.76
# #https://stackoverflow.com/questions/38015181/accuracy-score-valueerror-cant-handle-mix-of-binary-and-continuous-target
# #check out the link above , got good info about why u shldnt do this



# #Scatter plot
# #plt.scatter(df['a'],df['b'])
# #1 is malicious 0 is good


