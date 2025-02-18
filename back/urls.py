from django.urls import path
from .views import *

urlpatterns = [
    # --------------------------------------- back --------------------------------------

    path("course_details/<int:id>/",course_details, name='course_details'),
    path("degree_details/<int:id>/",degree_details, name='degree_details'),
    path("school_details/<int:id>/",school_details, name='school_details'),
    path("skill_details/<int:id>/",skill_details, name='skill_details')

# -------------------------------------------------------------------------------------

]
