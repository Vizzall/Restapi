from rest_framework import serializers
from .models import *

class employeeSerializer(serializers.ModelSerializer):

  class Meta:
      model= employee
      #fields=('first_name','last_name' )
      fields ='__all__'
 
