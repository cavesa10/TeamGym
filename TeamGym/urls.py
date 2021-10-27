from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appTeamGym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('refresh/', TokenRefreshView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view()),
    path('user/password/<int:pk>/', views.ChangePasswordView.as_view()),
    path('videos/<int:pk>/', views.VideosPlanesView.as_view()),
]