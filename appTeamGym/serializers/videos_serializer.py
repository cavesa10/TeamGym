from appTeamGym.models.videos import Videos
from appTeamGym.models.planes import Planes
from rest_framework import serializers

class Video_serializer(serializers.ModelSerializer):
    class Meta:  #sub-clase
        model = Videos
        fields = ['video_url','video_nombre']
