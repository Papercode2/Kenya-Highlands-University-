from django.db import models

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.name} at {self.submission_date}"


# Create your models here

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,default=12345)  # You should hash and store passwords securely

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Units(models.Model):
    Unit_Name = models.CharField(max_length=50)
    Unit_Code = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Nominals(models.Model):
    Student_Name= models.CharField(max_length=50)
    Student_ID = models.CharField(max_length=55)
    Course = models.CharField(max_length=15)
    Semester = models.IntegerField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"










