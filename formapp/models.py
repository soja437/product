from django.db import models

# Create your models here.
class employee(models.Model):
    emp_id = models.IntegerField(null=True)
    emp_name = models.CharField(max_length=255,null=True)
    emp_address = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
