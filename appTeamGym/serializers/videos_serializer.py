from rest_framework           import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from appTeamGym.models.planes import Planes
from appTeamGym.models.videos import Videos

class VideoSerializer(serializers.ModelSerializer):
    class Meta:  #sub-clase
        model = Videos
        fields = ['video_url','video_nombre','planes']

    def to_representation(self, obj):
        print(obj)
        video  = Videos.objects.get(video_id = obj.video_id)
        plan = Planes.objects.get(plan_id = video.planes_id)

        return{
            'id':           video.video_id,
            'video_url':    video.video_url,
            'video_nombre': video.video_nombre,
            'plan_id':      plan.plan_id,
        }