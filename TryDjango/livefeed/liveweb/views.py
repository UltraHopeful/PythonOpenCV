from django.shortcuts import render
from django.http import HttpResponse,StreamingHttpResponse
from django.views.decorators import gzip
import cv2
import time
from threading import *
from django.template import loader
from .models import VideoCamera


def index(request):
	return render(request,'liveweb/index.html')


cam = VideoCamera()
def gen(camera):
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@gzip.gzip_page
def livefe(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
