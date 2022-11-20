
import numpy as np
from flask import Flask,render_template,request
from keras.models import load_model


app = Flask(__name__)
model = load_model('crude_oil.h5',)

@app.route('/')
def home() :
    return render_template("index4.html")
@app.route('/about')
def home1() :
    return render_template("index4.html")
@app.route('/predict')
def home2() :
    return render_template("predict.html")

@app.route('/login',methods = ['POST'])
def login() :
    
    a=request.form['year1']
    b=request.form['year2']
    c=request.form['year3']
    d=request.form['year4']
    e=request.form['year5']
    f=request.form['year6']
    g=request.form['year7']
    h=request.form['year8']
    i=request.form['year9']
    j=request.form['year10']
    x_input = [a,b,c,d,e,f,g,h,i,j]
    for i in range(0, len(x_input)): 
        x_input[i] = float(x_input[i]) 
    print(x_input)
    x_input=np.array(x_input).reshape(1,-1)
    temp_input=list(x_input)
    temp_input=temp_input[0].tolist()
    lst_output=[]
    n_steps=10
    i=0
    while(i<1):
        
        if(len(temp_input)>10):
            x_input=np.array(temp_input[1:])
            print("{} day input {}".format(i,x_input))
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            yhat = model.predict(x_input, verbose=0)
            print("{} day output {}".format(i,yhat))
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            lst_output.extend(yhat.tolist())
            i=i+1
        else:
            x_input = x_input.reshape((1, n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            print(yhat[0])
            temp_input.extend(yhat[0].tolist())
            print(len(temp_input))
            lst_output.extend(yhat.tolist())
            i=i+1

    print(lst_output)
    
    
    return render_template("predict.html",showcase = 'The next day predicted value is:'+str(lst_output))
    
if __name__ == '__main__' :
    app.run(debug = True,port=5000)