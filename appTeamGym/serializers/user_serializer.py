from rest_framework import serializers
from appTeamGym.models.user import User
from appTeamGym.models.imc import Imc
from appTeamGym.models.planes import Planes
from appTeamGym.serializers.imc_serializer import imc_serializer
from rest_framework.relations import PrimaryKeyRelatedField

class UserSerializer(serializers.ModelSerializer):
  imc = imc_serializer(read_only=True)
  plan_id = PrimaryKeyRelatedField(queryset=Planes.objects.all(), required=False)
  class Meta:
    model = User
    fields = ['username', 'password', 'email', 'name', 'last_name','fecha_nacimiento', 'frequencia_fisica','objetivo_usuario','estatura','peso','genero','imc','plan_id']

  def create(self, validated_data):
    planId = validated_data.pop('plan_id')
    imcValues = validated_data.get('peso')/(validated_data.get('estatura')**2)
    planeObject = Planes.objects.get(plan_id=planId.plan_id)
    userInstance = User.objects.create(plan_id = planeObject,**validated_data)
    Imc.objects.create(user=userInstance, imc_value = imcValues)
    return userInstance
  # def update(self, validated_data):
  #   planId = validated_data.pop('plan_id')
  #   imcValues = validated_data.get('peso')/(validated_data.get('estatura')**2)
  #   planeObject = Planes.objects.get(plan_id=planId.plan_id)
  #   userInstance = User.objects.create(plan_id = planeObject,**validated_data)
  #   Imc.objects.create(user=userInstance, imc_value = imcValues)
  #   return userInstance
  def to_representation(self, value):
    user = User.objects.get(id=value.id)
    plan = Planes.objects.get(plan_id=value.id)
    imc = Imc.objects.get(user=value.id)
    return {
      'username': user.username,
      'email': user.email,
      'name': user.name,
      'last_name': user.last_name,
      'fecha_nacimiento': user.fecha_nacimiento,
      'frequencia_fisica': user.frequencia_fisica,
      'objetivo_usuario': user.objetivo_usuario,
      'estatura': user.estatura,
      'peso': user.peso,
      'genero': user.genero,
      'plan_id': plan.plan_id,
      'imc': {
        'imc_value': imc.imc_value,
        'fecha_registro': imc.fecha_registro,
      }
    }