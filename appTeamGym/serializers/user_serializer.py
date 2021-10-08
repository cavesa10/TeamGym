from rest_framework import serializers
from appTeamGym.models.user import User
from appTeamGym.models.imc import Imc
from appTeamGym.models.planes import Planes
from appTeamGym.serializers.imc_serializer import imc_serializer
#from appTeamGym.serializers.planes_serializer import planes_serializer

class UserSerializer(serializers.ModelSerializer):
  imc = imc_serializer()
  #planes = planes_serializer()
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'email', 'name', 'last_name','fecha_nacimiento', 'frequencia_fisica','objetivo_usuario','estatura','peso','genero','imc']

  def create(self, validated_data):
    imcData = validated_data.pop('imc') #sobrescritura, crear cuenta y usuarios
    #planesData = validated_data.pop('planes')
    userInstance = User.objects.create(**validated_data) # toma y elimina todas las
    Imc.objects.create(user=userInstance, **imcData)
    #Planes.objects.create(user=userInstance, **planesData)
    return userInstance
  def to_representation(self, obj):
    user = User.objects.get(id=obj.id)
    imc = Imc.objects.get(user=obj.id)
    return {
      'id': user.id,
      'username': user.username,
      'password': user.password,
      'email': user.email,
      'name': user.name,
      'last_name': user.last_name,
      'fecha_nacimiento': user.fecha_nacimiento,
      'frequencia_fisica': user.frequencia_fisica,
      'objetivo_usuario': user.objetivo_usuario,
      'estatura': user.estatura,
      'peso': user.peso,
      'genero': user.genero,
      'imc': {
        'imc_id': imc.imc_id,
        'imc_value': imc.imc_value,
      }

    }