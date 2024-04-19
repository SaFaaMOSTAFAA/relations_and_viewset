from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Student,Subject,Department
from .serializers import StudentSerializer,SubjectSerializer,DepartmentSerializer

# Create your views here.

class Viewset_Department(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer
  

class Viewset_subject(viewsets.ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer
    

class Viewset_Student(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer    




