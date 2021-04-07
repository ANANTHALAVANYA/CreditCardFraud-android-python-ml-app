# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:11:37 2020

@author: sudhakar
"""
from flask import Flask
import numpy as np
from flask import request, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index2():
    return render_template('index2.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        l=[]
        int_features=[] 
        
        age=request.json['age']
        l.append(age)
        int_features.append(int(age))
        ##
        sex=request.json['sex']
        l.append(sex)
        if sex=='FeMale':
            sex1=1
        else:
            sex1=0
        int_features.append(int(sex1))
        ##
        job=request.json['job']
        l.append(job)
        int_features.append(int(job))
        
        housing=request.json['housing']
        l.append(housing)
        if housing=='own':
            housing=0
        elif housing=='free':
            housing=1
        else:
            housing=2
        int_features.append(int(housing))
        
        saving_account=request.json['saving_account']
        l.append(saving_account)
        
        if saving_account=='little':
            saving_account=0
        elif saving_account=='moderate':
            saving_account=1
        else:
            saving_account=2
        int_features.append(int(saving_account))
        
        checking_account=request.json['check_acc']
        l.append(checking_account)
        if checking_account=='little':
            checking_account=0
        elif checking_account=='moderate':
            checking_account=1
        else:
            checking_account=2
        int_features.append(int(checking_account))
        
        credit_amount=request.json['credit_amt']
        l.append(credit_amount)
        int_features.append(int(credit_amount))
        
        duration=request.json['duration']
        l.append(duration)
        int_features.append(int(duration))
        
        purpose=request.json['purpose']
        l.append(purpose)
        if purpose=='car':
            purpose=0
        elif purpose=='radio/TV':
            purpose=1
        elif purpose=='furniture/equipment':
            purpose=2
        elif purpose=='business':
            purpose=3
        elif purpose=='education':
            purpose=4
        elif purpose=='repairs':
            purpose=5
        elif purpose=='vacation/others':
            purpose=6
        else:
            purpose=7
        int_features.append(int(purpose))
        
        print(int_features)
        final_features = [np.array(int_features)]
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        
        output = int(prediction)
        print(output)
        
        if output==0:
            
            '''return render_template('form1.html',
            prediction_text='your prediction result is negative so he is a fraud ',res=0)'''
            return{'message':'The person is a fraud'}
        else:
            
            #return render_template('form1.html',res=1,prediction_text='your prediction resut is positive so he is not a fraud ' )
            return{'message':'The person is not a fraud'}
if __name__=="__main__":
    app.run(debug=True,use_reloader=False)
