from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='homepage')
]

urlpatterns = [
    path('goody/', views.goody, name='goody')

]

