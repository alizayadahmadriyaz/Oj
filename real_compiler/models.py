from django.db import models

# Create your models here.

class CodeSubmission(models.Model):
    language=models.TextField()
    code=models.TextField()
    output_data=models.TextField(null=True,blank=True)
    input_data=models.TextField(null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)