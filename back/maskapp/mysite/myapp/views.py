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
    cv2.imwrite("input.jpeg", img)

    a = "hello django"
    return Response(a)

@csrf_exempt
@api_view(['GET'])
def test(request):
    a = "test!!!!"
    return Response(a)
