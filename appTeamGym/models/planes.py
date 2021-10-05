from django.db import models

class Planes(models.Model):
  plan_id = models.AutoField(primary_key=True)
  plan_nombre = models.CharField('planNombre',max_length=30)
