from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .planes import Planes


class UserManager(BaseUserManager):
  def create_user(self, username, password=None,):
    """
    Creates and saves a user with the given username and password.
    """
    if not username:
      raise ValueError('Users must have an username')
    user = self.model(username=username)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, username, password):
    """
    Creates and saves a superuser with the given username and password.
    """
    user = self.create_user(
      username=username,
      password=password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user


#model user
class User(AbstractBaseUser, PermissionsMixin):
  id = models.BigAutoField(primary_key=True)
  username = models.CharField('Username', max_length=15, unique=True)
  password = models.CharField('Password', max_length=256)
  email = models.EmailField('Email', max_length=100)
  name = models.CharField('Name', max_length=30)
  last_name = models.CharField('LastName',max_length=30)
  fecha_nacimiento = models.DateField()
  frequencia_fisica = models.CharField('FrequenciaFisica', max_length=30)
  objetivo_usuario = models.CharField('ObjetivoUsuario', max_length=30)
  estatura = models.DecimalField('Estatura',max_digits=5, decimal_places=2)
  peso = models.DecimalField('Peso',max_digits=5, decimal_places=1)
  genero = models.CharField('Genero', max_length=30)
  plan_id = models.ForeignKey(Planes, related_name='planes', on_delete=models.CASCADE)


  def save(self, **kwargs):
      print("Entre")
      some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
      self.password = make_password(self.password, some_salt)
      super().save(**kwargs)

  def _save(self, **kwargs):
      print("Entre")
      super().save(**kwargs)

  objects = UserManager()
  USERNAME_FIELD = 'username'
