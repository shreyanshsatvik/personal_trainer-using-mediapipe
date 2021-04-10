from flask import Flask, render_template, redirect, url_for, request, session, Response
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



def gen_frames():  
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


app=Flask(__name__)
app.config["DEBUG"]= True

@app.route('/',methods=["POST","GET"])
def home():

    return render_template("index.html")

@app.route('/squats',methods=["POST","GET"])
def squats():
    

    return render_template('squats.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

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
