from django.db import models

# Create your models here.
class Course(models.Model):
    Course_Name = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.Course_Name
    
class Student(models.Model):
    # Course_Name = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    Course_Name = models.CharField(max_length=100,null=True)
    usn = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    # Gender = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50,null=True)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    Branch = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return f"{self.name} - {self.usn} - {self.Course_Name}"



# class Enrollment(models.Model):
    # # USN = models.ForeignKey(Student, on_delete=models.CASCADE)
    # Course_Name = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment_Date = models.DateField()

    # def __str__(self):
    #     return f"{self.USN}"

    

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,null=True)
    massege = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return self.name

