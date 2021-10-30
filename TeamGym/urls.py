from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appTeamGym import views

urlpatterns = [
    path('refresh/', TokenRefreshView.as_view()),
    path('login/', TokenObtainPairView.as_view()), # Login de un usuario
    path('user/', views.UserCreateView.as_view()), # Registro de un usuario
    path('user/<int:pk>/', views.UserDetailView.as_view()),  # Detalles de un usuario
    path('user/update/<int:pk>/', views.UserUpdateView.as_view()), # Actualizar usuario Excepto contraseña y username
    path('user/password/<int:pk>/', views.ChangePasswordView.as_view()), # Actualizar contraseña
    path('videos/<int:pk>/', views.VideosPlanesView.as_view()), #Lista de videos por plan
    path('videos/', views.VideosCreateView.as_view()), # Crear un video
    path('video/<int:pk>/', views.VideoUpdateView.as_view()), # Actualizar un video
    path('video/delete/<int:pk>/', views.VideoDeleteView.as_view()), # Eliminar un video
    path('plan/<int:pk>/', views.PlanUpdateView.as_view()), # Actualizar un plan
    path('plan/', views.PlanCreateView.as_view()), # Crear un plan
    path('plan/deleted/<int:pk>/', views.PlanDeleteView.as_view()), # Eliminar un plan
]