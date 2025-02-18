from django.urls import path
from .views import *

urlpatterns = [
# -------------------------------------- front -----------------------------------------

    path("courses/",courses, name='courses'),
    path("degree/",degree, name='degree'),
    path("school/",school, name='school'),
    path("skill/",skill, name='skill'),

# -----------------------------------------------------------------------------------

]
