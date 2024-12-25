from flask import Flask,render_template,redirect,url_for,request,Request,Response
from PIL import Image 
import pickle
  
# loading in the model to predict on the data 
pickle_in = open('churn.pkl', 'rb') 
CH = pickle.load(pickle_in) 

welcome=Flask(__name__)

@welcome.route('/')
def app():
    return render_template('index.html')







if __name__=='__main__':
    welcome.run(debug=True)