from django.db import models

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=200)
    choice1 = models.TextField(null=True)
    choice2 = models.TextField(null=True)
    choice3 = models.TextField(null=True)
    choice4 = models.TextField(null=True)
    survey_at = models.DateTimeField(auto_now_add=True)