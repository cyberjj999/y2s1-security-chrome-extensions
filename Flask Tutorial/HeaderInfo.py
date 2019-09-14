# import requests
# url = "https://sg.todays-winner.club/todays-winner/?winner=101.127.33.110&prx=f8d5ff6d-d5a3-4d75-af07-e58000f618ff&isp=Starhub%20Internet%20Pte%20ltd&trd=interated-citeven.com&ver=1&cep=-HTGD06iCiKch2iF6LhxPmumNkXvxCZNPxqmH8wnlTcQG2HFePJUm2GvCmNzQYJNO2fD5PE1muApyo7fmpdAHr5hKCGahCIYX4mpB2ZrOK2ANiyWbBaI_VKtjuVGTgOA5nLOhi8rAA0OCteNT-L0NeoL32MOtoZueItVxaE3XBykWHFTgVhxp_q1dMXUFC9bZicAFpJSGDcqlZ0qyJZXG5dt4O2NVnxyKGhl-nCs2UZvmroPnNq-2IvdWJPo_ZA8KdELTUE7qyS6yH1YIy7o64ZsdlzBKXO34F4acKPVxSbytgdNXdamlxL9RG8pJg_LvfkmibAYexRZ6S8qVUWVclYggRkcF13iUKmhfpFHAbjFYJ_Hx0OFZ754sRxHXLWEeXwILR8c5ZxhDOogMhVNpbXA9cEFxqTi-hn1pVcsBSwkZA8yZ3eisJUdcFxto_2USkv-iliZFTkl8ULm6Q3BmSyC__awVyknwl6V7N-cd5nIvu4I0PeK22kl35htCaNFmUwkr3N3zapEHav0AlkiF28Ad3KdMSoIWey7nr0oxdI&lptoken=1593649c02cc96dc452b"
# resHead = requests.head(url)
# resGet = requests.get(url)

# #url length , content length , all these details are diff if i query a diff url
# print(resHead.headers.get('content-length'))
# print('charset is',resHead.headers.get('Content-Type'))
# print(resHead.headers.get('server'))
# print(resHead.headers.get('date'))

# print("The header info is below")
# print(resHead.headers)


# print(resGet.headers)

# # #If no http: will say invalid URL
# # #If got http will say Failed to establish a new connection , HTTPConnection object
# # #So essentially u can put , IF , this column is null , dont CHECK at ALL



# # import requests
# # import json

# # # Defining the api-endpoint
# # url = 'https://api.abuseipdb.com/api/v2/blacklist'

# # querystring = {
# #     'countMinimum':'15',
# #     'maxAgeInDays':'60',
# #     'confidenceMinimum':'90'
# # }

# # headers = {
# #     'Accept': 'application/json',
# #     'Key': 'bfc077a071029caf2c070e9b5c9189e69f6db76617bbce30f4deb15ba9d0114ddcc535e1c1882052'
# # }

# # response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# # # Formatted output
# # decodedResponse = json.loads(response.text)
# # print(json.dumps(decodedResponse, sort_keys=True, indent=4))

# #CHECK YOUR WHOIS API here
# # import requests
# # urlText = "https://www.fddsadssafas.com"


# # try:
# #     XMLWHOIS = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService", params={
# #     "apiKey" : "at_Tsc6W7NsPNdAJVq94MYhgPpPPUqir",
# #     "domainName": urlText,
# #     "outputFormat" : "JSON"
                    
                
# #     })
# #     urlCreatedDate = XMLWHOIS.json()['WhoisRecord']['createdDate']
# #     urlUpdatedDate = XMLWHOIS.json()['WhoisRecord']['updatedDate']
# #     urlCountry = XMLWHOIS.json()['WhoisRecord']['registrant']['countryCode']
# #     urlState = XMLWHOIS.json()['WhoisRecord']['registrant']['state']

# #     print('urlCreatedDate is ' ,urlCreatedDate)
# #     print('urlUpdatedDate is ' ,urlUpdatedDate)
# #     print('urlCountry is ' ,urlCountry)
# #     print('urlState is ' ,urlState)

# # except Exception as e:  # This is the correct syntax
# #     print("There is an error")
# #     urlCreatedDate = 'None'
# #     urlUpdatedDate = 'None'
# #     urlCountry = 'None'
# #     urlState = 'None'
# #     print('urlCreatedDate is ' ,urlCreatedDate)
# #     print('urlUpdatedDate is ' ,urlUpdatedDate)
# #     print('urlCountry is ' ,urlCountry)
# #     print('urlState is ' ,urlState)



import joblib
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
myLeCOUNTRY = joblib.load("preprocessingObjects/myLeCOUNTRY.pkl")
myLeSTATEPRO = joblib.load("preprocessingObjects/myLeSTATEPRO.pkl")
myLeUPDATE = joblib.load("preprocessingObjects/myLeUPDATE.pkl")
myLeREGDATE = joblib.load("preprocessingObjects/myLeREGDATE.pkl")
myOHEncoder = joblib.load("preprocessingObjects/OHEncoder.pkl")
myLeCHARSET = joblib.load("preprocessingObjects/myLeCHARSET.pkl")
print(myLeCOUNTRY.classes_)
print(myLeSTATEPRO.classes_)
print(myLeUPDATE.classes_)
print(myLeREGDATE.classes_)
print(myOHEncoder.active_features_)
print(myLeCHARSET.classes_)
