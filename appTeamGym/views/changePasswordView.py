from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
#from django.contrib.auth.models import User
from appTeamGym.models.user import User
from appTeamGym.serializers.changePasswordSerializer import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            self.object = self.get_object()
            print (self.object)
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                elif serializer.data.get("old_password") == serializer.data.get("new_password"):
                    return Response({"new_password": ["Old and new passwords are the same."]}, status=status.HTTP_400_BAD_REQUEST)
                newPassword = self.object
                newPassword.set_password(serializer.data.get("new_password"))
                newPassword._save() # el metodo _save actualiza la contraseña
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)