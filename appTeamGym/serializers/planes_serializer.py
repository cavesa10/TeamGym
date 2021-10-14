from appTeamGym.models.planes import Planes
from rest_framework import serializers
from appTeamGym.serializers.videos_serializer import Video_serializer

class planes_serializer(serializers.ModelSerializer):
    videos = Video_serializer(read_only=True, many=True)
    class Meta:  #sub-clase
        model = Planes
        fields = ['plan_id', 'plan_nombre', 'videos']
