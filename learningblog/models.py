from django.db import models

# Create your models here.

#Tuple to set the priority choices
# PRIORITY = [
#     ("H", "High"),
#     ("M", "Medium"),
#     ("L", "Low"),
# ]
# #Creating Questions model
# class Question(models.Model):
#     title                   = models.CharField(max_length=50)
#     question                = models.TextField(max_length=500)
#     priority                = models.CharField(max_length=1, choices=PRIORITY)
#
#     def __str__(self):
#         return self.title
