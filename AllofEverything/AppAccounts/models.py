from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.OneToOneField(User_name, on_delete=models.CASCADE)
    user_Id = models.CharField(max_length = 40)
    user_Loc = models.IntegerField()
    user_ModList = models.CharField(max_length = 40)
    