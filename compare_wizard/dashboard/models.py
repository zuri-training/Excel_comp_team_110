from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    file = models.FileField(upload_to='media/', blank=True, null=True)
    status = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


# class DocFile(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     file_one = models.FileField(upload_to='media/', blank=True, null=True)
#     file_two = models.FileField(upload_to='media/', blank=True, null=True)
#     file_viz = models.FileField(upload_to='media/', blank=True, null=True)