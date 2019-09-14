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

from matplotlib import style

#Read dataset , store it as data
data = pd.read_csv("dataset_000.csv")
j = 0
k = 0

#Store no. of Malicious and Benign website in j and k
#j contains number of malicious data
#k contains number of benign data
j = data.loc[data.Type == 1, 'Type'].count()
k = data.loc[data.Type == 0, 'Type'].count()
# Malicious : 216 - 12.13%
# Benign : 1565 - 0.88%
# Total 1781 

#Plot bar chart -> Not a very good representation
# objects = ('Malicious', 'Benign')
# y_pos = np.arange(len(objects))
# performance = [j,k]
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Number of data')
# plt.title('Comparison of malignant and benign data')
# plt.show()

#Plot pie chart
labels = 'Malicious','Benign'
sizes = [j,k]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
pylab.show()
