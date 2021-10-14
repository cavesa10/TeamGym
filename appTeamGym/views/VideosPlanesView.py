from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from appTeamGym.models.planes import Planes
from appTeamGym.serializers.planes_serializer import planes_serializer

class VideosPlanesView(generics.RetrieveAPIView):
    queryset = Planes.objects.all()
    serializer_class = planes_serializer
    permission_classes = (IsAuthenticated, )