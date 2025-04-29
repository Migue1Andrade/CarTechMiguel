from django.urls import path
from .views import home_view, edit_profile, create_post

urlpatterns = [
    path('home/', home_view, name='home'),
    path('editar-perfil/', edit_profile, name='edit_profile'),
	path('create/post', create_post, name='create-post'),
]
