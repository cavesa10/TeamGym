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
  def to_representation(self, value):
    user = User.objects.get(id=value.id)
    imcs = Imc.objects.filter(user=value.id).all()
    imcObj = []
    for imc in imcs:
      imcObj.append({
        'imc_value': imc.imc_value,
        'fecha_registro': imc.fecha_registro,
      })
    return {
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
      'plan_id': user.plan_id.plan_nombre,
      'imc': imcObj
    }
class UserUpdateSerializer(serializers.ModelSerializer):
  imc = imc_serializer(read_only=True)
  plan_id = PrimaryKeyRelatedField(queryset=Planes.objects.all(), required=False)
  class Meta:
    model = User
    exclude = ['username', 'password']
  def update(self,instance,validated_data ):
    planId = validated_data.pop('plan_id')
    planeObject = Planes.objects.get(plan_id=planId.plan_id)
    instance.email = validated_data.get('email')
    instance.name = validated_data.get('name')
    instance.last_name = validated_data.get('last_name')
    instance.fecha_nacimiento = validated_data.get('fecha_nacimiento')
    instance.frequencia_fisica = validated_data.get('frequencia_fisica')
    instance.objetivo_usuario = validated_data.get('objetivo_usuario')
    instance.genero = validated_data.get('genero')
    instance.plan_id = planeObject
    if instance.peso != validated_data.get('peso') or instance.estatura != validated_data.get('estatura'):
      instance.peso = validated_data.get('peso')
      instance.estatura = validated_data.get('estatura')
      print("hay cambios")
      imcValues = validated_data.get('peso')/(validated_data.get('estatura')**2)
      Imc.objects.create(user=instance, imc_value = imcValues)
    instance._save()
    return instance
  def to_representation(self, value):
    user = User.objects.get(id=value.id)
    imcs = Imc.objects.filter(user=value.id).all()
    imcObj = []
    for imc in imcs:
      imcObj.append({
        'imc_value': imc.imc_value,
        'fecha_registro': imc.fecha_registro,
      })
    return {
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
      'plan_id': user.plan_id.plan_nombre,
      'imc': imcObj
    }