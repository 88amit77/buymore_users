from django.db import models
from django.contrib.auth.models import Group


class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(Group)
