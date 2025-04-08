from django.urls import path
from .views import home_view, edit_profile

urlpatterns = [
    path('home/', home_view, name='home'),
    path('editar-perfil/', edit_profile, name='edit_profile'),
]
