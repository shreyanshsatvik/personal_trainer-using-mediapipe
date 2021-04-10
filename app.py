from flask import Flask, render_template, redirect, url_for, request, session, Response
import pandas as pd
import numpy as np
import logging
import datetime
import os.path
from flask import Markup
import os
import cv2
import mediapipe as mp



# def gen_frames():  
#     camera = cv2.VideoCapture(0)
#     while True:
#         success, frame = camera.read()  # read the camera frame
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


app=Flask(__name__)
app.config["DEBUG"]= True

@app.route('/',methods=["POST","GET"])
def home():

    return render_template("index.html")

@app.route('/squats',methods=["POST","GET"])
def squats():
    from squats import squats
    count,calories = squats(5)
    print("Count",count)
    print("Calories",calories)

    return render_template('squats.html',count = count,calories = calories)

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/pushup',methods=["POST","GET"])
def pushups():
    from push_up import pushup
    count,calories = pushup(5)
    print("Count",count)
    print("Calories",calories)
    return render_template('pushup.html',count = count,calories = calories)

@app.route('/pullup',methods=["POST","GET"])
def pullups():
    from pull_up import pullup
    count,calories = pullup(5)
    print("Count",count)
    print("Calories",calories)
    return render_template('pullup.html',count = count,calories = calories)
@app.route('/biceps',methods=["POST","GET"])
def biceps():
    from weight_lifting import biceps
    count,calories = biceps(5)
    print("Count",count)
    print("Calories",calories)

    return render_template('weight_lifting.html',count = count,calories = calories)


@app.route('/crunches',methods=["POST","GET"])
def crunches():
    from crunches import crunches
    count,calories = crunches(5)
    print("Count",count)
    print("Calories",calories)
    return render_template('crunches.html',count = count,calories = calories)

@app.route('/count',methods=["POST","GET"])
def count():
    return render_template('count.html')

if __name__ == '__main__': 

    app.run()
