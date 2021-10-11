from django.db import models
from .user import User

class Imc(models.Model):
  imc_id = models.AutoField(primary_key=True)
  imc_value = models.IntegerField('imcValue')
  user = models.ForeignKey(User, related_name='imc', on_delete=models.CASCADE)