from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend

from django.http import request
from rest_framework.serializers import Serializer


from appTeamGym.models.planes import Planes
from appTeamGym.serializers.plan_serializer import PlanSerializer
from appTeamGym.models.user import User


class PlanCreateView(generics.CreateAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated, )


    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        user = User.objects.get(id=valid_data['user_id'])

        if user.is_superuser == False:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = PlanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response("Plan creado exitosamente", status=status.HTTP_201_CREATED)

class PlanUpdateView(generics.UpdateAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated, )


    def put(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        user = User.objects.get(id=valid_data['user_id'])

        if user.is_superuser == False:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().put(request, *args, **kwargs)

class PlanDeleteView(generics.DestroyAPIView):
    queryset = Planes.objects.all()
    serializer_class = PlanSerializer
    permission_classes = (IsAuthenticated, )

    def delete(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)
        user = User.objects.get(id=valid_data['user_id'])

        if user.is_superuser == False:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)