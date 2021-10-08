from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from appTeamGym.models.user import User
from appTeamGym.serializers.user_serializer import UserSerializer


class UserDeletedView(generics.RetrieveAPIView):
    queryset = User.objects.all() # obtiene el modelo seleccionado
    serializer_class = UserSerializer # serializa la info recibido
    permission_classes = (IsAuthenticated, )

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return {"Message": "Item has been deleted"}