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

app=Flask(name)
app.config["DEBUG"]= True

@app.route('/',methods=["POST","GET"])
def home():

    return render_template("index.html")

@app.route('/squats',methods=["POST","GET"])
def squats():

@app.route('/pushup',methods=["POST","GET"])
def pushups():

@app.route('/pullups',methods=["POST","GET"])
def pullups():

@app.route('/biceps',methods=["POST","GET"])
def biceps():

@app.route('/crunches',methods=["POST","GET"])
def crunches():


@app.route('/',methods=["POST","GET"])
def pushup():


if name == 'main': 

    app.run()
