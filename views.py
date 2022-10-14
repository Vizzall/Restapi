from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers  import *


class employeeList_1(APIView):
     def get (self,request,id):
        employee1=employee.objects.get(id=id)
        serializer=employeeSerializer(employee1)
        return Response(serializer.data)
      
class employeeList_2(APIView):      

   def get(self,request):
       employee1=employee.objects.all()
       serializer=employeeSerializer(employee1,many=True)
       return Response(serializer.data)
       
   def post(self,request):
       if request.data.get("id",None):
          rem=employee.objects.get(id=request.data.get("id"))
          rem.delete()
          return Response({"Particular_Data":"Deleted"})
          take=request.data
       employee.objects.create(firstname=take['firstname'],lastname=take['lastname'],emp_id=take['emp_id'])
       return Response({'Status': 'Done Successfully'})
       
       
       
   def delete(self,request):
       employee.objects.all().delete()
       return Response({'Status': 'Deleted Successfully'})
       
       
   def put(self,request):
       req_data = request.data
       upd = employeeSerializer(employee.objects.get(id=req_data["id"]),req_data)
       if upd.is_valid():
          upd.save()
          return Response({"Updated":"Successfully"})
       else:
            print(post)
            return Response({"Data":"Does not exist"})           
         
