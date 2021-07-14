import numpy as np
import pandas as pd
from flask import request
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#DataFlair - Read the data
df=pd.read_csv('parkinsons.data')

#DataFlair - Get the features and labels
features=df.loc[:,df.columns!='status'].values[:,1:]
labels=df.loc[:,'status'].values

#DataFlair - Get the count of each label (0 and 1) in labels
print(labels[labels==1].shape[0], labels[labels==0].shape[0])

#DataFlair - Scale the features to between -1 and 1
scaler=MinMaxScaler((-1,1))
x=scaler.fit_transform(features)
y=labels

#DataFlair - Split the dataset
x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=0.2, random_state=7)

#DataFlair - Train the model
model=XGBClassifier()
model.fit(x_train,y_train)

# DataFlair - Calculate the accuracy
y_pred=model.predict(x_test)


inputStr= request.form['Parameters']
inputArr=inputStr.split(',')
inputData=tuple(inputArr)
inpNumpy = np.asarray(inputData)
inpReshapped = inpNumpy.reshape(1, -1)
stdData = scaler.transform(inpReshapped)
prediction = model.predict(stdData)

if (prediction[0] == 0):
    result="The person is healthy"
else:
    result="The person is suffering from Parkinson's disease"
print(result)
# from sklearn.svm import SVC
# sv = SVC(kernel='linear').fit(x_train,y_train)
# pickle.dump(sv , open('result.pkl' , 'wb'))