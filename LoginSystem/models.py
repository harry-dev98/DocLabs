from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserData(models.Model):
    patient=models.ForeignKey(User,on_delete=models.CASCADE)
    reports=models.ImageField(upload_to='pics')
    disease=models.TextField(max_length=100)
    def __str__(self):
        return self.patient.username

