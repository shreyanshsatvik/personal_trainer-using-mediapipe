from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
import numpy as np
import logging
import datetime
import os.path
from flask import Markup
import os
from push_up import pushup
from pull_up import pullup

app=Flask(__name__)
app.config["DEBUG"]= True

@app.route('/',methods=["POST","GET"])
def home():

    return render_template("index.html")

@app.route('/squats',methods=["POST","GET"])
def squats():
    return render_template("squats.html")


@app.route('/pushup',methods=["POST","GET"])
def pushups():
    pass
@app.route('/pullups',methods=["POST","GET"])
def pullups():
    pass
@app.route('/biceps',methods=["POST","GET"])
def biceps():
    pass

@app.route('/crunches',methods=["POST","GET"])
def crunches():
    pass

@app.route('/',methods=["POST","GET"])
def pushup():
    pass

if __name__ == '__main__': 

    app.run()
