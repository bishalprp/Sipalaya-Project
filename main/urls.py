from django.urls import path
from .views import *

urlpatterns = [
# ========================================for main part ====================================================== 
    path("",index, name='index'),
    path("about/",about, name='about'),
    path("contact/",contact, name='contact'),
    path("team/",team, name='team'),
    path("testimonial/",testimonial, name='testimonial')

# ==============================================================================================================

]