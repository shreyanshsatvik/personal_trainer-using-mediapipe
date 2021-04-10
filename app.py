from flask import Flask, render_template, redirect, url_for, request, session
import pandas as pd
import numpy as np
import logging
import datetime
import os.path
from flask import Markup
import os

app=Flask(__name__)
app.config["DEBUG"]= True

@app.route('/',methods=["POST","GET"])
def home():
    return render_template("index.html")


if __name__ == '__main__': 

    app.run()


