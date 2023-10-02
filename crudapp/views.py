from django.shortcuts import render
from django.http import HttpResponse
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
class list_one(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Hellomodel.objects.all()
    serializer_class=HelloSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class list_two(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Hellomodel.objects.all()
    serializer_class=HelloSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)