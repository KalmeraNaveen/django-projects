from rest_framework import serializers
from crudapp.models import *
class HelloSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hellomodel
        fields='__all__'