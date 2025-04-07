from django.urls import path
from .views import login_view, register_view
from veiculos.views import home_view

urlpatterns = [
    path('', login_view, name='login'),
]

urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
	path('home/', home_view, name='home')
]
