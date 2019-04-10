from django.db import models
from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import time
from threading import *

cascPath = 'C:/Users/Ultra_Hopeful/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml'  # dataset
faceCascade = cv2.CascadeClassifier(cascPath)

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0+cv2.CAP_DSHOW)
        (self.grabbed, self.frame) = self.video.read()
        Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (209, 255, 26), 2)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
