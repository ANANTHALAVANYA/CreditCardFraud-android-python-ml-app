# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:17:45 2020

@author: sudhakar
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:45:43 2020

@author: RAMYA
"""
#from sklearn.preprocessing import LabelEncoder
#import numpy as nm
#import matplotlib.pyplot as plt
import pandas as pd
import pickle
#from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
#import seaborn as sns
from sklearn.linear_model import LogisticRegression 
#from sklearn.preprocessing import StandardScaler 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report 
from imblearn.over_sampling import SMOTE 
#from sklearn.decomposition import PCA 
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import chi2_contingency
from sklearn.naive_bayes import GaussianNB
import warnings
def remove_outlier(df_in, col_name):
    df1=df_in.loc['good'==df_in['Risk']]
    q1 = df1[col_name].quantile(0.25)
    q3 = df1[col_name].quantile(0.75)
    print("q1 is",q1)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out1 = df1.loc[(df1[col_name] > fence_low) & (df1[col_name] < fence_high)]
    df2=df_in.loc['bad'==df_in['Risk']]
    q1 = df2[col_name].quantile(0.25)
    q3 = df2[col_name].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_out2 = df2.loc[(df2[col_name] > fence_low) & (df2[col_name] < fence_high)]
    return df_out1.append(df_out2)
def SMOTE1(df):
    y=df.Risk
    x=df.drop('Risk',axis=1)
    os= SMOTE(random_state=20)
    os_data_x,os_data_y=os.fit_sample(x,y)  
    pd.DataFrame(data=os_data_x,columns=x.columns)
    pd.DataFrame(data=os_data_y,columns=['Risk'])
    x_train,x_test,y_train,y_test=train_test_split( os_data_x,os_data_y,test_size=0.20,random_state=100)
    return x_train,x_test,y_train,y_test
def lr(df,smote):
    print(df)
    L1=LogisticRegression()
    #Train the model
    if smote=='True':
        x_train,x_test,y_train,y_test=SMOTE1(df)
    else:
        y=df.Risk
        x=df.drop('Risk',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
        
    L1.fit(x_train,y_train)
    #predicting outcome
    y_pre_L1=L1.predict(x_test)
    #print(classification_report(y_test,y_pre_L1)) 
    #print("Accuracy percentage LR:"+"{:.2f}".format(accuracy_score(y_test,y_pre_L1)*100))
    #confusion matrix
    #cm = confusion_matrix(y_test, y_pre_L1)
    #print(cm)
    return round(accuracy_score(y_test,y_pre_L1)*100)
def svc(df,smote):
    S=SVC()
    if smote=='True':
        x_train,x_test,y_train,y_test=SMOTE1(df)
    else:
        y=df.Risk
        x=df.drop('Risk',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
    #Train the model
    S.fit(x_train,y_train)
    #predicting outcome
    y_pre_S=S.predict(x_test)
    print(classification_report(y_test,y_pre_S)) 
    print("Accuracy percentage SVC:"+"{:.2f}".format(accuracy_score(y_test,y_pre_S)*100))
    #confusion matrix
    cm = confusion_matrix(y_test, y_pre_S)
    print(cm)
    return accuracy_score(y_test,y_pre_S)*100
def dtc(df,smote):
    DTC=DecisionTreeClassifier()
    if smote=='True':
        x_train,x_test,y_train,y_test=SMOTE1(df)
    else:
        y=df.Risk
        x=df.drop('Risk',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=100)
    DTC.fit(x_train,y_train)
    #predicting outcome
    y_pre_DTC=DTC.predict(x_test)
    print(classification_report(y_test,y_pre_DTC)) 
    print("Accuracy percentage DTC:"+"{:.2f}".format(accuracy_score(y_test,y_pre_DTC)*100))
    #confusion matrix
    cm = confusion_matrix(y_test, y_pre_DTC)
    print(cm)
    return accuracy_score(y_test,y_pre_DTC)*100
def gnbAlg(df,smote):
    gnb = GaussianNB()
    #Train the model
    if smote=='True':
        x_train,x_test,y_train,y_test=SMOTE1(df)
    else:
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=100)
        
    gnb.fit(x_train,y_train)
    #predicting outcome
    y_pre_gnb=gnb.predict(x_test)
    print(classification_report(y_test,y_pre_gnb)) 
    print("Accuracy percentage GNB:"+"{:.2f}".format(accuracy_score(y_test,y_pre_gnb)*100))
    #confusion matrix
    cm = confusion_matrix(y_test, y_pre_gnb)
    print(cm)
    return accuracy_score(y_test,y_pre_gnb)*100
def knc(df,smote):
    ##KNeighborsClassifier
    y=df.Risk
    x=df.drop('Risk',axis=1)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=100)
    KNC=KNeighborsClassifier()
    #Train the model
    KNC.fit(x_train,y_train)
    #predicting outcome
    y_pre_KNC=KNC.predict(x_test)
    print(classification_report(y_test,y_pre_KNC)) 
    print("Accuracy percentage KNC:"+"{:.2f}".format(accuracy_score(y_test,y_pre_KNC)*100))
    #confusion matrix
    cm = confusion_matrix(y_test, y_pre_KNC)
    print(cm)
    return accuracy_score(y_test,y_pre_KNC)*100
def chi_sqaure(i,j):
    table=pd.crosstab(i,j) 
    stat,p,dof,expected=chi2_contingency(table)
    print(p)
    alpha=0.05
    if p<=alpha:
        return True
    else:
        return False
warnings.simplefilter("ignore")
df=pd.read_csv('german_credit_data.csv')
df=df.drop('No',axis=1)
print(df)
#print(df.isnull().sum())
# =============================================================================
#replacing null values
df1=df.loc[df['Risk']=='good']
df1['Saving accounts'].fillna(str(df1['Saving accounts'].mode().values[0]),inplace=True)
df1['Checking account'].fillna(str(df1['Checking account'].mode().values[0]),inplace=True)
df2=df.loc[df['Risk']=='bad']
df2['Saving accounts'].fillna(str(df2['Saving accounts'].mode().values[0]),inplace=True)
df2['Checking account'].fillna(str(df2['Checking account'].mode().values[0]),inplace=True)
df=df1.append(df2)

'''print(df)
#########Correlation

plt.figure(figsize=(10,5))
ax=sns.heatmap(df.corr(),annot=True)
bottom, top = ax.get_ylim()
ax.set_ylim(bottom+0.5, top - 0.5)

print(df.isnull().sum())
'''
'''print(sns.boxplot(x=df["Age"]))
print(sns.boxplot(x=df['Duration']))
print(sns.boxplot(x=df["Credit amount"]))'''
df=remove_outlier(df,'Credit amount')
#print(sns.boxplot(x=df["Credit amount"]))
df=remove_outlier(df,'Age')
df=remove_outlier(df,'Duration')
#print(sns.boxplot(x=df["Duration"]))
df=remove_outlier(df,'Duration')
#print(sns.boxplot(x=df["Duration"]))

#print(df)
l=[]
l2=[]
print(df.dtypes)
##chi-square
for i in df:
    if df[i].dtype!='object':
        l2.append(i)
    else:
        l.append(i)
for i in l:
    d=chi_sqaure(df['Risk'],df[i])
    if d==True:
        print(i)
    elif d==False:
        print(i)
        df=df.drop(i,axis=1)

df['Saving accounts'] = df['Saving accounts'].map({"little":0,"moderate":1,"quite rich":2 ,
       "rich":3 });
df['Checking account'] = df['Checking account'].map({"little":0,"moderate":1,"quite rich":2 ,
       "rich":3 });
df['Sex'] = df['Sex'].map({"male":0,"female":1}).astype(int);
df['Housing'] = df['Housing'].map({"own":0,"free":1,"rent":2}).astype(int);
df['Risk'] = df['Risk'].map({'good':1,'bad':0}).astype(int);
df['Purpose'] = df['Purpose'].map({"car":0,"radio/TV":1,"furniture/equipment":2 ,
       "business":3,"education":4,"repairs":5,"vacation/others":6 ,
       "domestic appliances":7});
'''df1=pd.DataFrame()
for i in l2:
    df1[i]=df[i]
plt.figure(figsize=(20,5))
print(df)'''
#print(df)
#print(sns.boxplot(x=df["Credit amount"]))
train,test=train_test_split(df,test_size=0.2)
y=df.Risk
x=df.drop('Risk',axis=1)
os= SMOTE(random_state=20)
os_data_x,os_data_y=os.fit_sample(x,y)  
pd.DataFrame(data=os_data_x,columns=x.columns)
pd.DataFrame(data=os_data_y,columns=['Risk'])
x_train,x_test,y_train,y_test=train_test_split( os_data_x,os_data_y,test_size=0.20,random_state=100)
RF=RandomForestClassifier()
#Train the model
RF.fit(x_train,y_train)
# Saving model to disk
pickle.dump(RF, open('model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
#print(model.predict([[2, 9, 6]]))

















