from django.db import models
from django.contrib import admin
class Bankloan(models.Model):
  name=models.CharField(max_length=100)
  accno=models.IntegerField(primary_key="accno")
  ifscno=models.IntegerField()
  mobno=models.IntegerField()
  email=models.EmailField()
   
class BankloanAdmin(admin.ModelAdmin):
  list_display=('name','accno','ifscno','mobno','email')
 

