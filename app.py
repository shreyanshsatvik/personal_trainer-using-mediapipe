from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
import numpy as np
import logging
import datetime
import os.path
from flask import Markup
import os

from pull_up import pullup
import cv2
import mediapipe as mp

app=Flask(__name__)
app.config["DEBUG"]= True

@app.route('/',methods=["POST","GET"])
def home():

    return render_template("index.html")

@app.route('/squats',methods=["POST","GET"])
def squats():
    from squats import squats
    count,calories = squats()
    print("Count",count)
    print("Calories",calories)

    return render_template('squats.html')



@app.route('/pushup',methods=["POST","GET"])
def pushups():
    from push_up import pushup
    count,calories = pushup()
    print("Count",count)
    print("Calories",calories)
    return render_template('pushup.html')

@app.route('/pullup',methods=["POST","GET"])
def pullups():
    from pull_up import pullup
    count,calories = pullup()
    print("Count",count)
    print("Calories",calories)
    return render_template('pullup.html')
@app.route('/biceps',methods=["POST","GET"])
def biceps():
    from weight_lifting import biceps
    count,calories = biceps()
    print("Count",count)
    print("Calories",calories)

    return render_template('weight_lifting.html')


@app.route('/crunches',methods=["POST","GET"])
def crunches():
    from crunches import crunches
    count,calories = crunches()
    print("Count",count)
    print("Calories",calories)
    return render_template('crunches.html',count = count,calories = calories)

if __name__ == '__main__': 

    app.run()
