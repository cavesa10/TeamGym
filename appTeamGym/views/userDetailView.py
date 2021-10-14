from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from appTeamGym.models.user import User
from appTeamGym.serializers.user_serializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all() # obtiene el modelo seleccionado
    serializer_class = UserSerializer # serializa la info recibido
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        if valid_data['user_id'] != kwargs['pk']: # compara id solicitante y a consultar
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse,
                            status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)