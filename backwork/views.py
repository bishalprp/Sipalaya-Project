from django.shortcuts import render
from .models import CourseDetails

# Create your views here.

# ---------------------------------------- backwork -------------------------------------------------

def course_details(request):
    cou_d=CourseDetails.objects.all()
    context={
        'cou_d':cou_d
    }
    return render(request,'course_details.html',context)

def degree_details(request):
    return render(request, 'degree_details.html')

def school_details(request):
    return render(request, 'school_details.html')

def skill_details(request):
    return render(request, 'skill_details.html')

# -------------------------------------------------------------------------------------------------------------