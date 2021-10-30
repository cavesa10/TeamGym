from django.conf import settings
from rest_framework import generics, status
from django.http import request
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated


from appTeamGym.models.videos import Videos
from appTeamGym.models.user import User
from appTeamGym.serializers.videos_serializer import VideoSerializer

class VideosCreateView(generics.CreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideoSerializer
    model = User
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None):
            obj = self.request.user
            return obj

    def post(self, request, *args, **kwargs):
        user = self.object = self.get_object()
        print (user.is_superuser)
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)

        print("requestaData",request.data)
        print("valid, data",valid_data)
        if user.is_superuser == False:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'status': 'success',
            'message': 'Video guardados exitosamente',
        }
        return Response(response, status=status.HTTP_201_CREATED)
