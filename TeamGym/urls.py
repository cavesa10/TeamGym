from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appTeamGym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UserCreateView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]