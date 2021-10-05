from django.db import models
from .planes import Planes

class Videos(models.Model):
  video_id = models.AutoField(primary_key=True)
  video_url = models.CharField('videoURL',max_length=250)
  video_nombre = models.CharField('VideoNombre',max_length=50)
  planes = models.ForeignKey(Planes, related_name='videos', on_delete=models.CASCADE)
