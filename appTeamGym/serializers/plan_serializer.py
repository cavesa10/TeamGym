from appTeamGym.models.planes import Planes
from rest_framework import serializers

class PlanSerializer(serializers.ModelSerializer):
    class Meta:  #sub-clase
        model = Planes
        fields = ['plan_id', 'plan_nombre']