import numpy as np
from flask import Flask,render_template
import joblib
from flask import request

app = Flask(__name__)
nb_model_snowfall = joblib.load("snowfall_prediction.pkl")

@app.route('/')
def prem():
    return render_template('index.html')

@app.route('/',methods=["POST"])
def home1():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    arr = np.array([[data1,data2,data3,data4,data5,data6]],dtype= float)
    pred = nb_model_snowfall.predict(arr)
    if pred[0] > 0:
       return render_template('index.html',prediction_text = f" YES (tomorrow will be snowfall)")
    else:
        return render_template('index.html',prediction_text = f" NO (tomorrow will not be snowfall) ")
        
    # return render_template('index.html',prediction_text = "{:.2f}°C".format(pred[0]))
    # "{:.2f}".format(a)

if __name__ == "__main__":
    app.run(debug=True)