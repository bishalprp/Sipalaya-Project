from django.urls import path
from .views import *

urlpatterns = [
    path("private/",private, name='private'),
    path("terms/",terms, name='terms'),
    path("help/",help, name='help'),
    path("/",basemail, name='basemail')
]
