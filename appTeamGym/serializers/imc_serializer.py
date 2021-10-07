from appTeamGym.models.imc import Imc
from rest_framework import serializers

class imc_serializer(serializers.ModelSerializer):
    class Meta:  #sub-clase
        model = Imc
        fields = ['imc_id', 'imc_value']