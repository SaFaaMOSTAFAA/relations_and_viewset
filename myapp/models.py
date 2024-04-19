from django.db import models


# Create your models here.
class Department(models.Model) :
   
    name= models.CharField(max_length=40)

    def __str__(self) :
        return self.name   
    
class Subject(models.Model):
    name=models.CharField(max_length=30)
    teacher=models.CharField(max_length=50)
    department=models.ForeignKey(Department,related_name='subjects',on_delete=models.CASCADE)

    def __str__(self) :
        return self.name    
    
class Student(models.Model) :
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    department=models.ForeignKey(Department,related_name='departmentforstudents',on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='students')

    def __str__(self) :
        return self.name
    


    
 
