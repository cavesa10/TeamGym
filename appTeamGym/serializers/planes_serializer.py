from appTeamGym.models.planes import Planes
from rest_framework import serializers
from appTeamGym.serializers.videos_serializer import VideoSerializer

class planes_serializer(serializers.ModelSerializer):
    videos = VideoSerializer(read_only=True, many=True)
    class Meta:  #sub-clase
        model = Planes
        fields = ['plan_id', 'plan_nombre', 'videos']
