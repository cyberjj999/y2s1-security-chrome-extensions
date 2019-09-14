from flask import Flask, url_for , request ,jsonify
from flask_cors import CORS
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model , preprocessing
from sklearn.preprocessing import OneHotEncoder
import pickle
import json
import requests
import whois
import datetime
import pytz
import csv
from sklearn.externals import joblib
from sklearn.preprocessing import Normalizer
from datetime import datetime as dt


app = Flask(__name__)
#This program is created through flask documentation - http://flask.pocoo.org/docs/1.0/quickstart/
#First do $env:FLASK_APP = "hello.py"
#Then do python -m flask run
#CORS(app)

#whoisURL = "https://hexillion.com/samples/WhoisXML/?query=https%3A%2F%2Fwww.google.com&_accept=application%2Fvnd.hexillion.whois-v2%2Bjson/"
#WHOISGet = requests.get(whoisURL)
#data = WHOISGet.json()
#print(data)

# response = requests.get("https://jsonwhois.com/api/v1/whois",

#    headers={
#       "Accept": "application/json",
#         "Authorization": "Token token=0228a83eeb3720f602d90da56e3990fb"
#       },

#    params={
#        "domain": "www.google.com"
#     })

#print(response.json()['created_on']) # The parsed response
#print(response.json()['updated_on'])


# XMLWHOIS = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService", params={
#        "apiKey" : "at_C0fHXMVHPFuUesgev3ccffRf7okNS",
#        "domainName": "www.google.com",
#        "outputFormat" : "JSON"
    
    
#     })
    
    


# print(XMLWHOIS.json()['WhoisRecord']['createdDate'])
# print(XMLWHOIS.json()['WhoisRecord']['updatedDate'])
# print(XMLWHOIS.json()['WhoisRecord']['registrant']['countryCode'])
# print(XMLWHOIS.json()['WhoisRecord']['registrant']['state'])



#http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4
#Super helpful , can get Server , Content-Length
# MitOpenCourseUrl = "http://www.youtube.com"
# resHead = requests.head(MitOpenCourseUrl)
# resGet = requests.get(MitOpenCourseUrl,stream=True)
#resHead.headers['Content-Length'] # output 169
#print(resHead.headers['Content-Type'])
# resGet.headers.get('content-length')

#print(resHead.headers.get('content-length'))
#print(resHead.headers)
#resGet.headers['Content-Length'] # output 121291539
#print(resGet.headers)

#@app.route('/',methods=['POST'])
#Apparently cant use methods=post idk why
@app.route('/', methods=['GET','POST'])
def process_URL():
    if request.method == "POST":
        #data = request.get_json() returns URL : Value
        #The below returns the value only
        
        urlText = request.get_json()['URLText']
        #print("URL Text received is " , urlText)
        #urlCharset = request.get_json()['Charset']
        urlLength = len(urlText)
        #print(urlLength)
        special_char = '!@#$%^&*()-=_+[]\{\}|;\':",./<>?`~'
        urlNumOfSpecChar= 0
        for sub_str in urlText:
            for c in special_char:
                if c in sub_str:
                    urlNumOfSpecChar += 1
        #Declare request to get header information of the URL
        #resHead = requests.head(urlText)

        try:
            #If this pass ,means its a LEGIT website 
            resHead = requests.head(urlText)
            urlCharsetH = resHead.headers.get('Content-Type')
            #print(urlCharsetH)
            if isinstance(urlCharsetH, str):
                urlCharsetH = urlCharsetH.replace("text/html; charset=","")
            elif urlCharsetH == 'TEXT/HTML':
                urlCharsetH = 'NONE'
            else:  
                urlCharsetH = 'None'
            # urlCharsetH = resHead.headers['Content-Type'].replace("text/html; charset=","")
                
            #Have to use .get , cus sometimes no content length , if u use
            #.get u will return none , instead of having key error
            urlContentLengthH = resHead.headers.get('content-length')
            if urlContentLengthH is None:
                checkCLNone = 'Yes'
                urlContentLengthH = float(-1)
                #urlContentLengthH.astype(float)

            else:
                urlContentLengthH = float(urlContentLengthH)
                checkCLNone = 'No'

            urlServerH = resHead.headers.get('Server')
            
            if urlServerH is None:
                urlServerH = 'None'
            
            try:
                urlCharsetH = urlCharsetH.upper()
                urlServerH = urlServerH.upper()

                XMLWHOIS = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService", params={
                "apiKey" : "at_6SWI9OjVLBdxb40JCOWyykUk7y7Jx",
                "domainName": urlText,
                "outputFormat" : "JSON"
            })

                urlCreatedDate = XMLWHOIS.json()['WhoisRecord']['createdDate']
                urlUpdatedDate = XMLWHOIS.json()['WhoisRecord']['updatedDate']
                urlCountry = XMLWHOIS.json()['WhoisRecord']['registrant']['countryCode']
                urlState = XMLWHOIS.json()['WhoisRecord']['registrant']['state']
            #rmb to convert the detail to uppercase , i scare got error
                # urlCreatedDate = '2014-02-21T10:45:07-0800'
                # urlUpdatedDate = '2018-02-21T10:45:07-0800'
                # urlCountry = 'US'
                # urlState = 'AK'   

                ts10 = datetime.datetime.today() - datetime.timedelta(days=10*365) #old
                ts1 = datetime.datetime.today() - datetime.timedelta(days=365) #very new
                ts5 = datetime.datetime.today() - datetime.timedelta(days=5*365) #very Old for reg date
                ts0 = datetime.datetime.today() - datetime.timedelta(days=30) #newest
                #tsnow = datetime.datetime.today()
                # data.loc[data['WHOIS_UPDATED_DATE'] <= noneFormatter , 'WHOIS_UPDATE_FORMATTED'] = 'None' #10 years ago (prolly solid)
                # data.loc[(data['WHOIS_UPDATED_DATE'] <= ts10) & (data['WHOIS_UPDATED_DATE'] > noneFormatter), 'WHOIS_UPDATE_FORMATTED'] = 'VeryOld' #10 years ago (prolly solid)
                # data.loc[(data['WHOIS_UPDATED_DATE'] <= ts3) & (data['WHOIS_UPDATED_DATE'] > ts10), 'WHOIS_UPDATE_FORMATTED'] = 'Old'
                # data.loc[(data['WHOIS_UPDATED_DATE'] <= ts0) & (data['WHOIS_UPDATED_DATE'] > ts1), 'WHOIS_UPDATE_FORMATTED'] = 'New'
                # data.loc[(data['WHOIS_UPDATED_DATE'] <= tsnow) & (data['WHOIS_UPDATED_DATE'] > ts0), 'WHOIS_UPDATE_FORMATTED'] = 'VeryNew'

                urlRegFormattedDate = pd.to_datetime(urlCreatedDate,format='%Y-%m-%d')
                urlRegFormattedDate = urlRegFormattedDate.to_pydatetime()
                urlRegFormattedDate = urlRegFormattedDate.replace(tzinfo=None)

                if (urlRegFormattedDate <= ts10):
                    regOutput = 'VeryOld'
                elif ( (urlRegFormattedDate <= ts1) & (urlRegFormattedDate > ts10) ):
                    regOutput = 'Old'
                elif ( (urlRegFormattedDate <= ts0) & (urlRegFormattedDate > ts1) ):
                    regOutput = 'New'
                # elif ( (urlRegFormattedDate <= tsnow) & (urlRegFormattedDate > ts0) ):
                #     regOutput = 'veryNew'
                else:
                    regOutput = "NA"

                urlUpdatedFormattedDate = pd.to_datetime(urlUpdatedDate,format='%Y-%m-%d')
                urlUpdatedFormattedDate = urlUpdatedFormattedDate.to_pydatetime()
                urlUpdatedFormattedDate = urlUpdatedFormattedDate.replace(tzinfo=None)

                if (urlUpdatedFormattedDate <= ts5):
                    updateOutput = 'VeryOld'
                elif ( (urlUpdatedFormattedDate <= ts1) & (urlUpdatedFormattedDate > ts5) ):
                    updateOutput = 'Old'
                elif ( (urlUpdatedFormattedDate <= ts0) & (urlUpdatedFormattedDate > ts1) ):
                    updateOutput = 'New'
                # elif ( (urlUpdatedFormattedDate <= tsnow) & (urlUpdatedFormattedDate > ts0) ):
                #     updateOutput = 'veryNew'
                else:
                    updateOutput = "NA"
              


                myLeSERVER = joblib.load("preprocessingObjects/myLeSERVER.pkl")

                if urlServerH not in myLeSERVER.classes_:
                    urlServerH = 'Others'

                myLeCHARSET = joblib.load("preprocessingObjects/myLeCHARSET.pkl")

                if urlCharsetH not in myLeCHARSET.classes_:
                    urlCharsetH = 'NONE'

                urlResult = 0
                                                                                                                                                       
                urlData = [["URL_LENGTH","NUMBER_SPECIAL_CHARACTERS","CHARSET","SERVER","CONTENT_LENGTH","CONTENT_LENGTH_NONE","WHOIS_COUNTRY","WHOIS_STATEPRO","WHOIS_REGDATE_FORMATTED","WHOIS_UPDATE_FORMATTED","Type"]
                ,[urlLength,urlNumOfSpecChar,urlCharsetH,urlServerH,urlContentLengthH,checkCLNone,urlCountry,urlState,regOutput,updateOutput,urlResult]]
                with open('C:/Users/jiaju/Desktop/Recovery Files Check/Year 2 Sem 1/Network Security & Project/Project/Flask Tutorial/extractedFeatures.csv', 'w',newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(urlData)
                csvFile.close()
                print(urlData)
                df = pd.read_csv('extractedFeatures.csv')
                #Is not issue of writing to CSV file
                #I tested with a test csv file alr , so its CONFIRM ohe
                #print(df.head())

                #END HERE
                
                #SERVER LE , i put ontop to check smth
                myLeCOUNTRY = joblib.load("preprocessingObjects/myLeCOUNTRY.pkl")
                myLeSTATEPRO = joblib.load("preprocessingObjects/myLeSTATEPRO.pkl")
                myLeUPDATE = joblib.load("preprocessingObjects/myLeUPDATE.pkl")
                myLeREGDATE = joblib.load("preprocessingObjects/myLeREGDATE.pkl")
                myLeCONTENTL_NONE = joblib.load("preprocessingObjects/myLeCONTENTL_NONE.pkl")

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

                df['CHARSET'] = myLeCHARSET.transform(df['CHARSET'])
                df['SERVER'] = myLeSERVER.transform(df['SERVER'])
                df['WHOIS_COUNTRY'] = myLeCOUNTRY.transform(df['WHOIS_COUNTRY'])
                df['WHOIS_STATEPRO'] = myLeSTATEPRO.transform(df['WHOIS_STATEPRO'])
                df['WHOIS_UPDATE_FORMATTED'] = myLeUPDATE.transform(df['WHOIS_UPDATE_FORMATTED'])
                df['WHOIS_REGDATE_FORMATTED'] = myLeREGDATE.transform(df['WHOIS_REGDATE_FORMATTED'])
                df['CONTENT_LENGTH_NONE'] = myLeCONTENTL_NONE.transform(df['CONTENT_LENGTH_NONE'])

                X = df[["URL_LENGTH","NUMBER_SPECIAL_CHARACTERS","CHARSET","SERVER","CONTENT_LENGTH","CONTENT_LENGTH_NONE","WHOIS_COUNTRY","WHOIS_STATEPRO",'WHOIS_REGDATE_FORMATTED','WHOIS_UPDATE_FORMATTED']].values
                print("X values are ",X)
                #X = [[241421,2444,1,14,-1,1,31,22,0,0]]
                #issue is WITH OHE , no matter what value of X i give to it,
                #it still returns the same probability

                #sc_X.transform(X)
                

                #.cut in pandas , to bin #eg old not so old , new  , 10 yrs , 5 yrs ,3 yrs 1 yrs ,                 
                ohe = joblib.load("preprocessingObjects/OHencoder.pkl")
                #ohe = OneHotEncoder(categorical_features=[2,3,4,5,6,13],handle_unknown='ignore')
                #print("My OHE active feature " , ohe.active_features_)

                #print("My X is now ", X)
                X = ohe.transform(X).toarray()
                #print("My X is after ohe", X)
    
                #THIS LITERALLY SCREWD ME UP FOR A DAY OR 2 , I THOUGHT WHY I KEEP GETTING SAME
                #RESULT , ITS BECAUSE OF THIS , IF I DONT RESHAPE IT WILL KEEP GIVING ME SAME RESULT
                #sc_X = preprocessing.StandardScaler()
                #X = sc_X.fit_transform(X)
                sc_X = joblib.load("preprocessingObjects/scaler.pkl")
                X = sc_X.transform(X.reshape(1, -1))
                #print("X value is " , X)
                #https://stackoverflow.com/questions/45012271/getting-correct-shape-for-datapoint-to-predict-with-a-regression-model-after-usi
                #super helpful link above , help solve the issue of one hot encoding

                # #print(predicted)
                # if predicted == [1]:
                #     result = "bad"
                # else:
                #     result = "good"
                # print(data)
                pickle_in = open("MaliciousLinkModel.pickle" , "rb")
                #opening the model u saved
                model = pickle.load(pickle_in)
                predicted = model.predict(X)
                model_probs = model.predict_proba(X)
                print("Probability of 0 and 1 " ,model_probs)
                print("If i only take [:1]" , model.predict_proba(X)[:,1])

                print(predicted)
                if (model_probs[:,1]>0.2):
                    return jsonify("Bad")
                else:
                    return jsonify("Good")

                    #First try is to catch the .header response

            except Exception as e:  # This is the correct syntax
                #To catch the issue with WHOIS api
                print("The exception is " , e)
                updateOutput = 'None'
                regOutput = 'None'
                urlCountry = 'NONE'
                urlState = 'NONE'
                #The caps matter here , my date label encode with small letter 'None'
                #My country and state is with big letters , so yea.

                urlResult = 'good'

                myLeCHARSET = joblib.load("preprocessingObjects/myLeCHARSET.pkl")
                myLeSERVER = joblib.load("preprocessingObjects/myLeSERVER.pkl")
                
                #delete this later
                #urlCharsetH = 'UTF-8'

                if urlServerH not in myLeSERVER.classes_:
                    urlServerH = 'Others'
                if urlCharsetH not in myLeCHARSET.classes_:
                    urlCharsetH = 'NONE'

                urlData = [["URL_LENGTH","NUMBER_SPECIAL_CHARACTERS","CHARSET","SERVER","CONTENT_LENGTH","CONTENT_LENGTH_NONE","WHOIS_COUNTRY","WHOIS_STATEPRO","WHOIS_REGDATE_FORMATTED","WHOIS_UPDATE_FORMATTED","Type"]
                ,[urlLength,urlNumOfSpecChar,urlCharsetH,urlServerH,urlContentLengthH,checkCLNone,urlCountry,urlState,regOutput,updateOutput,urlResult]]
                with open('C:/Users/jiaju/Desktop/Recovery Files Check/Year 2 Sem 1/Network Security & Project/Project/Flask Tutorial/extractedFeatures.csv', 'w',newline='') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(urlData)
                csvFile.close()
                print(urlData)
                df = pd.read_csv('extractedFeatures.csv')

                #CHARSET LE put on top also                 
                #SERVER LE , i put ontop to check smth

                myLeCOUNTRY = joblib.load("preprocessingObjects/myLeCOUNTRY.pkl")
                myLeSTATEPRO = joblib.load("preprocessingObjects/myLeSTATEPRO.pkl")
                myLeUPDATE = joblib.load("preprocessingObjects/myLeUPDATE.pkl")
                myLeREGDATE = joblib.load("preprocessingObjects/myLeREGDATE.pkl")
                myLeCONTENTL_NONE = joblib.load("preprocessingObjects/myLeCONTENTL_NONE.pkl")

                df['CHARSET'] = myLeCHARSET.transform(df['CHARSET'])
                df['SERVER'] = myLeSERVER.transform(df['SERVER'])
                df['WHOIS_COUNTRY'] = myLeCOUNTRY.transform(df['WHOIS_COUNTRY'])
                df['WHOIS_STATEPRO'] = myLeSTATEPRO.transform(df['WHOIS_STATEPRO'])
                df['WHOIS_UPDATE_FORMATTED'] = myLeUPDATE.transform(df['WHOIS_UPDATE_FORMATTED'])
                df['WHOIS_REGDATE_FORMATTED'] = myLeREGDATE.transform(df['WHOIS_REGDATE_FORMATTED'])
                df['CONTENT_LENGTH_NONE'] = myLeCONTENTL_NONE.transform(df['CONTENT_LENGTH_NONE'])

                X = df[["URL_LENGTH","NUMBER_SPECIAL_CHARACTERS","CHARSET","SERVER","CONTENT_LENGTH","CONTENT_LENGTH_NONE","WHOIS_COUNTRY","WHOIS_STATEPRO",'WHOIS_REGDATE_FORMATTED','WHOIS_UPDATE_FORMATTED']].values
                #print("X values are ",X)
                #sc_X.transform(X)
               
                #.cut in pandas , to bin #eg old not so old , new  , 10 yrs , 5 yrs ,3 yrs 1 yrs ,                 
                ohe = joblib.load("preprocessingObjects/OHencoder.pkl")

                #ohe = OneHotEncoder(categorical_features=[2,3,4,5,6,13],handle_unknown='ignore')
                X = ohe.transform(X).toarray()
               
                #X = df[["URL_LENGTH","NUMBER_SPECIAL_CHARACTERS","CHARSET","SERVER","CONTENT_LENGTH","CONTENT_LENGTH_NONE","WHOIS_COUNTRY","WHOIS_STATEPRO",'WHOIS_REGDATE_FORMATTED','WHOIS_UPDATE_FORMATTED']].values
                # sc_X = preprocessing.StandardScaler()
                # X = sc_X.fit_transform(X)
                sc_X = joblib.load("preprocessingObjects/scaler.pkl")
                X = sc_X.transform(X.reshape(1, -1))

                pickle_in = open("MaliciousLinkModel.pickle" , "rb")
                #opening the model u saved
                #print("X value is " , X)
                model = pickle.load(pickle_in)
                
                predicted = model.predict(X)
                model_probs = model.predict_proba(X)
                print("Probability of 0 and 1 " ,model_probs)
                print("If i only take [:1]" , model.predict_proba(X)[:,1])
                print(predicted)
                if (model_probs[:,1]>0.2):
                    return jsonify("Bad")
                else:
                    return jsonify("Good")
                print("error is" , e)
                # print("Second error here!:" , e)
                # return jsonify("There is a problem") #2nd one didnt work this will run
            
            #Second try is to catch the WHOIS response
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print("error is" , e)
            return jsonify("No such website")
        #https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
        #Super helpful link above , to help with the try catch issue
        
        
    else:
        dataReceived = "no data received"
        print(dataReceived)
        return dataReceived

@app.route('/hello', methods=['GET','POST'])
def hello():
    if request.method == "POST":
        #data = request.get_json() returns URL : Value
        #The below returns the value only
        
        urlText = request.get_json()['URLText']
        #print("URL Text received is " , urlText)
        #urlCharset = request.get_json()['Charset']
        urlLength = len(urlText)
        #print(urlLength)
        special_char = '!@#$%^&*()-=_+[]\{\}|;\':",./<>?`~'
        urlNumOfSpecChar= 0
        for sub_str in urlText:
            for c in special_char:
                if c in sub_str:
                    urlNumOfSpecChar += 1
      
        resHead = requests.head(urlText)
        urlCharsetH = resHead.headers.get('Content-Type')
        if isinstance(urlCharsetH, str):
            urlCharsetH = urlCharsetH.replace("text/html; charset=","")
        elif urlCharsetH == 'TEXT/HTML':
            urlCharsetH = 'NONE'
        else:  
            urlCharsetH = 'None'

        urlContentLengthH = resHead.headers.get('content-length')
        if urlContentLengthH is None:
            checkCLNone = 'Yes'
            urlContentLengthH = float(-1)

        else:
            urlContentLengthH = float(urlContentLengthH)
            checkCLNone = 'No'

        urlServerH = resHead.headers.get('Server')
            
        if urlServerH is None:
            urlServerH = 'None'
            
        try:
            urlCharsetH = urlCharsetH.upper()
            urlServerH = urlServerH.upper()

            XMLWHOIS = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService", params={
            "apiKey" : "at_6SWI9OjVLBdxb40JCOWyykUk7y7Jx",
            "domainName": urlText,
            "outputFormat" : "JSON"
            })

            urlCreatedDate = XMLWHOIS.json()['WhoisRecord']['createdDate']
            urlUpdatedDate = XMLWHOIS.json()['WhoisRecord']['updatedDate']
            urlCountry = XMLWHOIS.json()['WhoisRecord']['registrant']['countryCode']
            urlState = XMLWHOIS.json()['WhoisRecord']['registrant']['state']
            #rmb to convert the detail to uppercase , i scare got error
            # urlCreatedDate = '2014-02-21T10:45:07-0800'
            # urlUpdatedDate = '2018-02-21T10:45:07-0800'
            # urlCountry = 'US'
            # urlState = 'AK'   
            ts10 = datetime.datetime.today() - datetime.timedelta(days=10*365) #old
            ts1 = datetime.datetime.today() - datetime.timedelta(days=365) #very new
            ts5 = datetime.datetime.today() - datetime.timedelta(days=5*365) #very Old for reg date
            ts0 = datetime.datetime.today() - datetime.timedelta(days=30) #newest
            
            urlRegFormattedDate = pd.to_datetime(urlCreatedDate,format='%Y-%m-%d')
            urlRegFormattedDate = urlRegFormattedDate.to_pydatetime()
            urlRegFormattedDate = urlRegFormattedDate.replace(tzinfo=None)

            urlRegFormattedDate = urlRegFormattedDate.strftime('%d/%m/%Y %H:%M')


            # if (urlRegFormattedDate <= ts10):
            #     regOutput = 'VeryOld'
            # elif ( (urlRegFormattedDate <= ts1) & (urlRegFormattedDate > ts10) ):
            #     regOutput = 'Old'
            # elif ( (urlRegFormattedDate <= ts0) & (urlRegFormattedDate > ts1) ):
            #     regOutput = 'New'
            # else:
            #     regOutput = "NA"



            urlUpdatedFormattedDate = pd.to_datetime(urlUpdatedDate,format='%Y-%m-%d')
            urlUpdatedFormattedDate = urlUpdatedFormattedDate.to_pydatetime()
            urlUpdatedFormattedDate = urlUpdatedFormattedDate.replace(tzinfo=None)

            #
            urlUpdatedFormattedDate = urlUpdatedFormattedDate.strftime('%d/%m/%Y %H:%M')

            #

            fields = [urlText,urlLength,urlNumOfSpecChar,urlCharsetH,urlServerH,urlContentLengthH,urlCountry,urlState,urlRegFormattedDate,urlUpdatedFormattedDate]

            # if (urlUpdatedFormattedDate <= ts5):
            #     updateOutput = 'VeryOld'
            # elif ( (urlUpdatedFormattedDate <= ts1) & (urlUpdatedFormattedDate > ts5) ):
            #     updateOutput = 'Old'
            # elif ( (urlUpdatedFormattedDate <= ts0) & (urlUpdatedFormattedDate > ts1) ):
            #     updateOutput = 'New'
            # else:
            #     updateOutput = "NA"
              


            myLeSERVER = joblib.load("preprocessingObjects/myLeSERVER.pkl")

            if urlServerH not in myLeSERVER.classes_:
                urlServerH = 'Others'

            myLeCHARSET = joblib.load("preprocessingObjects/myLeCHARSET.pkl")

            if urlCharsetH not in myLeCHARSET.classes_:
                urlCharsetH = 'NONE'
            
            # fields = [urlText,urlLength,urlNumOfSpecChar,urlCharsetH,urlServerH,urlContentLengthH,checkCLNone,urlCountry,urlState,regOutput,updateOutput]
            #print("my field is " , fields)
            with open('C:/Users/jiaju/Desktop/Recovery Files Check/Year 2 Sem 1/Network Security & Project/Project/Flask Tutorial/falsePositive.csv', 'a',newline='') as csvFile2:
                writer = csv.writer(csvFile2)
                writer.writerow(fields)

            return jsonify('Hello World') 

        except Exception as e:  # This is the correct syntax
            print("The exception is " , e)
            updateOutput = 'None'
            regOutput = 'None'
            urlCountry = 'NONE'
            urlState = 'NONE'
                #The caps matter here , my date label encode with small letter 'None'
                #My country and state is with big letters , so yea.
            myLeCHARSET = joblib.load("preprocessingObjects/myLeCHARSET.pkl")
            myLeSERVER = joblib.load("preprocessingObjects/myLeSERVER.pkl")
                
            # if urlServerH not in myLeSERVER.classes_:
            #     urlServerH = 'Others'
            # if urlCharsetH not in myLeCHARSET.classes_:
            #     urlCharsetH = 'NONE'

            #see if u want to record off the raw data instead , thn u change preprocessing
            #during training phrase
           
            fields = [urlText,urlLength,urlNumOfSpecChar,urlCharsetH,urlServerH,urlContentLengthH,urlCountry,urlState,regOutput,updateOutput]
            with open('C:/Users/jiaju/Desktop/Recovery Files Check/Year 2 Sem 1/Network Security & Project/Project/Flask Tutorial/falsePositive.csv', 'a',newline='') as csvFile2:
                writer = csv.writer(csvFile2)
                writer.writerow(fields)

            return jsonify("Hello World")
   



if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run(host= '0.0.0.0', port = 5000)
    #app.run()  # Launch built-in web server and run this Flask webapp

