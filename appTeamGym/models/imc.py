from django.db import models
from .user import User

class Imc(models.Model):
  imc_id = models.AutoField(primary_key=True)
  imc_value = models.DecimalField('imcValue',max_digits=5, decimal_places=3)
  fecha_registro = models.DateField( auto_now = True)
  user = models.ForeignKey(User, related_name='imc', on_delete=models.CASCADE)