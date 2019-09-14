import datetime
import pandas as pd
import pytz
from datetime import datetime as dt
import requests

utc=pytz.UTC

someDate = '12/05/1996 0:00'
anotherDate = '2018-02-21T10:45:07-0800'

ts1 = pd.to_datetime('1/1/2000')
print(type(ts1))




ts2 = pd.to_datetime('1/1/2030')
#X must be greater than ts3 , smaller than ts2
ts3 = pd.to_datetime('1/1/1990')
#ts20 = datetime.datetime.today() - datetime.timedelta(days=20*365) #very old

formattedDate = pd.to_datetime(anotherDate,format='%Y-%m-%d')
formattedDate = formattedDate.to_pydatetime()
formattedDate = formattedDate.replace(tzinfo=None)

ts1 = formattedDate.strftime('%d/%m/%Y %H:%M')


print(ts1)

print("my ts1 is ",ts1)
print(type(ts1))
#naive = ts5.replace(tzinfo=None)

# print(ts5)
# print(type(ts5))

# print(ts5 < ts20)


#print(ts4 < ts20)
#ts5 = datetime.datetime.strptime("2008-09-03T20:56:35.450686Z", "%Y-%m-%dT%H:%M:%S.%fZ")

#print(ts4) 
#print(ts5)

#print(ts4 <= ts20 )
# print(ts3 < datetime.datetime.today() < ts2)
# x = 25
# if x > 20 & x < 30:
#     print('yes')
# else:
#     print('no')
# X = datetime.datetime.today() - datetime.timedelta(days=20*365)
# print(X)


ts20 = datetime.datetime.today() - datetime.timedelta(days=20*365) #very old
ts10 = datetime.datetime.today() - datetime.timedelta(days=10*365) #old
ts3 = datetime.datetime.today() - datetime.timedelta(days=3*365) #new
ts1 = datetime.datetime.today() - datetime.timedelta(days=365) #very new
ts0 = datetime.datetime.today() - datetime.timedelta(days=7) #newest
tsnow = datetime.datetime.today()


print(formattedDate <= ts20)
print( (formattedDate <= ts10) & (formattedDate > ts20) )
print( (formattedDate <= ts3) & (formattedDate > ts10) )
print( (formattedDate <= ts1) & (formattedDate > ts3) )
print( (formattedDate <= ts0) & (formattedDate > ts1) )
print("===")
print( (formattedDate <= tsnow) & (formattedDate > ts0) )

if (formattedDate <= ts20):
    print("Longer than 20 yrs")
elif ( (formattedDate <= ts10) & (formattedDate > ts20) ):
    print("Between 10 and 20 years")
elif ( (formattedDate <= ts3) & (formattedDate > ts10) ):
    print("Between 3 and 10 years")
elif ( (formattedDate <= ts1) & (formattedDate > ts3) ):
    print("Between 1 and 3 years")
elif ( (formattedDate <= ts0) & (formattedDate > ts1) ):
    print("Between 7 days and 1 year")
elif ( (formattedDate <= tsnow) & (formattedDate > ts0) ):
    print("Between now and 7 days")


urlText = 'https://www.google.com'

resHead = requests.head(urlText)
#urlCharsetH = resHead.headers['Content-Type'].replace("text/html; charset=","")
                
#Have to use .get , cus sometimes no content length , if u use
#.get u will return none , instead of having key error
urlContentLengthH = resHead.headers.get('content-length')
print(type(urlContentLengthH))
if urlContentLengthH is None:
    print("OOPS")
else:
    print("wtf")

