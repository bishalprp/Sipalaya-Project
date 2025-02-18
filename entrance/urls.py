from django.urls import path
from .views import *

urlpatterns = [
     # entrance
    path('create_entrance/<int:course_id>/', create_entrance, name='create_entrance'),
    path('update_entrance/<int:entrance_id>/', update_entrance, name='update_entrance'),
    path('detele_entrance/<int:entrance_id>/', detele_entrance, name='detele_entrance'),

    # question
    path('create_question/<int:entrance_id>/',
         create_question, name='create_question'),
    path('update_question/<int:entrance_id>/<int:question_id>/',
         update_question, name='update_question'),


    path('delete_question/<int:entrance_id>/<int:question_id>/',
         delete_question, name='delete_question'),


    # entrance for student
    path('show_entrance/<int:course_id>/', show_entrance, name='show_entrance'),
    path('show_entrance_question/<int:entrance_id>/',
         show_entrance_question, name='show_entrance_question'),

    #     show result

    path('show_result/', show_result, name='show_result'),


]
