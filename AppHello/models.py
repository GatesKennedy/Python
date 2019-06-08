from django.db import models
'''
# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20, on_delete=models.CASCADE)
    user_password = models.CharField(max_length=40, on_delete=models.CASCADE)
#    user_Id = models.CharField(max_length = 40)
#    user_Loc = models.ForeignKey(max_length = 40)
#    user_ModList = models.CharField(max_length = 40)
'''
'''
class Input(models.Model):
    input_name = models.CharField(max_length=20, on_delete=models.CASCADE)
    input_password = models.CharField(max_length=40, on_delete=models.CASCADE)
    #blah
'''