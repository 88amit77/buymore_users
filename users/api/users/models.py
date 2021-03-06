from django.db import models
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import JSONField

class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(Group)


class Import(models.Model):

    import_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    imfile_name = models.CharField(max_length=50,null=True, blank=True)
    imfile_type = models.IntegerField(default=2) # 2-> Full Import 1-> partial import
    imfile_section = models.CharField(max_length=50)
    imfile_subsection = models.CharField(max_length=50, null=True, blank=True)
    imfile_size =models.FloatField(default=0.0)
    imfile_url = models.FileField(upload_to='import', max_length=100, blank=True, null=True)
    imfile_errorlog = models.CharField(max_length=200, null=True, blank=True)
    imfile_isread = models.BooleanField(default=False)
    imfile_iscompleted = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)


class Export(models.Model):
    export_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True, blank=True)
    file_type = models.CharField(max_length=200, null=True, blank=True)
    query_params = models.CharField(max_length=200, null=True, blank=True)
    exfile_name = models.CharField(max_length=50, null=True, blank=True)
    exfile_size = models.FloatField(default=0.0)
    exfile_path = models.CharField(max_length=200, null=True, blank=True)
    exfile_url = models.TextField(null=True, blank=True)
    exfile_url_time = models.DateTimeField(max_length=200, null=True, blank=True)
    exfile_errorlog = models.CharField(max_length=200, null=True, blank=True)
    exfile_iscreated = models.BooleanField(default=False)
    exfile_isdownloaded = models.BooleanField(default=False)
    status = models.CharField(max_length=50, default='')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
