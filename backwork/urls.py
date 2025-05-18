from django.urls import path
from .views import *
urlpatterns = [
    path("course_details/", course_details, name='coursedetails'),
    # path("degree_details/<int:id>/", degree_details, name='degree_details'),
    path("degree_details/", degree_details, name='degree_details'),
    path("school_details/", school_details, name='school_details'),
    path("skill_details/", skill_details, name='skill_details')
]

