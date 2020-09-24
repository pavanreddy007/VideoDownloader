from django.shortcuts import render
from rest_framework import views

from .serializers import UD_Serializer
from rest_framework.response import Response

from uapi.youtube import *

# Create your views here.

class Youtube_downloader(views.APIView):

	def post(self,request):

		serial=UD_Serializer(data=request.data)

		if serial.is_valid():

			x=serial.data

			print(x['file'],"serial data")

			y=x['file'].split(',')

			path=Download(y)

			return Response(path)

		return Response("please check the input")



