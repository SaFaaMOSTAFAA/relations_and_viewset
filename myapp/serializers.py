from rest_framework import serializers
from .models import Student,Subject,Department


class SubjectSerializer(serializers.ModelSerializer) :
      
    class Meta:
        model=Subject
        fields=['id','name','teacher','department'] 

class StudentSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model=Student
        fields=['id','name','age','department','subjects']        


class DepartmentSerializer(serializers.ModelSerializer): 
    subjects=SubjectSerializer(many=True,read_only=True)   

    class Meta:
        model=Department
        fields=['id','name','subjects']

  





       

   

   

