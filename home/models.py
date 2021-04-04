from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Plant(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_disease = models.CharField(max_length=255, null=True)
    disease_remedies = models.CharField(max_length=255, null=True)
    
    