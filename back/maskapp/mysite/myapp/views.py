from django.shortcuts import render
from rest_framework import status
from rest_framework .decorators import api_view
from rest_framework.response import Response
import json

from django.views.decorators.csrf import csrf_exempt

from PIL import Image
import cv2
import numpy as np
import base64
import io
#from sklearn.externals import joblib
import joblib

# Create your views here.

def get_hog(size):
    winSize = (size, size)
    blockSize = (16,16)
    blockStride = (8,8)
    cellSize = (8,8)
    nbins = 9
    derivAperture = 1
    winSigma = -1.
    histogramNormType = 0
    L2HysThreshold = 0.2
    gammaCorrection = 1
    nlevels = 64
    signedGradients = True

    hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,histogramNormType,L2HysThreshold,gammaCorrection,nlevels, signedGradients)
    return hog


def imageProcessing(size):
    img = cv2.imread("input.jpg",)
    height, width, channel = img.shape
    svm = joblib.load('maskSVM-1.pkl')
    hog = get_hog(size)

    if width > height: radius = int(height * 21 / 100)
    else : radius = int(width * 21 / 100)

    side = int(radius*90/100)
    centerX = int(width/2)
    centerY = int(height/2)

    trim_img = img[centerY-side:centerY+side, centerX-side:centerX+side]
    trim_img_gray = cv2.cvtColor(trim_img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontface.xml')
    face_locations = face_cascade.detectMultiScale(trim_img_gray)

    if len(face_locations) > 0:
        return "red"
    else:
        trim_img = cv2.resize(trim_img, dsize=(size, size), interpolation=cv2.INTER_AREA)
        hog_feature = hog.compute(trim_img)
        hog_feature = np.array(hog_feature).flatten().tolist()
        y_pred = svm.predict([hog_feature])
        if y_pred[0] == 1:
            return "blue"
        else:
            return "yellow"


@csrf_exempt
@api_view(['POST'])
def index(request):
    #print(type(request.body))
    data = json.loads(request.body)
    #print(data)
    #print(type(data["image"]))

    head, imgdata = data["image"].split(',')

    imgdata = base64.b64decode(str(imgdata))
    image = Image.open(io.BytesIO(imgdata))
    img = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    cv2.imwrite("input.jpg", img)
    result = imageProcessing(80)
    return Response(result)

@csrf_exempt
@api_view(['GET'])
def test(request):
    a = "test!!!!"
    return Response(a)
