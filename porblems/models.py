from django.db import models

# Create your models here.

class problemm(models.Model):
    problem_name = models.CharField(max_length=100)
    # problem_description = models.CharField(max_length=500)
    problem_description = models.TextField()
    # problem_code = models.CharField(max_length=2000)
    problem_input=models.TextField(default=0)
    problem_output=models.TextField(default=0)
    problem_diff=models.CharField(max_length=200)

class solution(models.Model):
    problem=models.ForeignKey(problemm,on_delete=models.CASCADE)
    verdict=models.CharField(max_length=200)
    submission_date=models.DateTimeField(auto_now_add=True)

class Test_Case(models.Model):
    Input=models.CharField(max_length=5000)
    Output=models.CharField(max_length=5000)
    problem=models.ForeignKey(problemm,on_delete=models.CASCADE)
