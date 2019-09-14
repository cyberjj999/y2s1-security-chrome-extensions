import pickle
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import numpy as np


pickle_in = open("MaliciousLinkModel.pickle" , "rb")
model = pickle.load(pickle_in)
                
X = [[4,31,4,2,-1,2,2,11,3,2]]
ohe = joblib.load("preprocessingObjects/OHencoder.pkl")
X = ohe.transform(X).toarray()
print(X)
                #print("My X is after ohe", X)

# sc_X = preprocessing.StandardScaler()
# X = sc_X.fit_transform(X)

sc_X = joblib.load("preprocessingObjects/scaler.pkl")
X = sc_X.transform(X.reshape(1, -1))
# X = sc_X.fit_transform(X)
#opening the model u saved
predicted = model.predict(X)
model_probs = model.predict_proba(X)
print("Probability of 0 and 1 " ,model_probs)
print("If i only take [:1]" , model.predict_proba(X)[:,1])

print(predicted)
#the sample data prediction is  [[0.03407602 0.96592398]]