import numpy as np
from flask import Flask,render_template, request
from keras.models import load_model
import tensorflow as tf
# tf.logging.set_verbosity(tf.logging.ERROR)
app = Flask(__name__)
model = load_model('crude_oil.h5',)
@app.route('/')
def home():
  return "wornig"
@app.route('/predict')
def predict():
  return "<h1>working</h1>"

if __name__ == '__main__' :
    app.run(debug = True)  

