from django.shortcuts import render
from django.http import HttpResponse
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

def accessControl(svm, size):


def imageProcessing(img):
    img = cv2.imread("input.jpg")
    height, width, channel = img.shape
    svm = joblib.load('lib/maskSVM-1.pkl')
    return access_control(svm, 80)

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
    a = "hello django"
    return Response(a)

@csrf_exempt
@api_view(['GET'])
def test(request):
    a = "test!!!!"
    return Response(a)
