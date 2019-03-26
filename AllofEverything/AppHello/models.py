from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length = 20)
    user_Id = models.CharField(max_length = 40)
    user_Loc = models.ForeignKey(max_length = 40)
    user_ModList = models.CharField(max_length = 40)
    