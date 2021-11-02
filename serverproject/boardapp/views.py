from django.http.response import HttpResponse
#from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BoardSerializer 
from .models import Board

class BoardViewSet(viewsets.ModelViewSet): 
    queryset = Board.objects.all() 
    serializer_class = BoardSerializer


