from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('bio', views.bio, name='bio' )
]