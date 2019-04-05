from django.db import models

# Create your models here.
class CampUrls(models.Model):
  CampUrl = models.CharField(max_length = 100)
    
class CampData(models.Model):
  CampGround= models.CharField(max_length = 40)
  CampUrl = models.ForeignKey(CampUrls, on_delete=models.CASCADE)
  CampEmail = models.CharField(max_length = 60)