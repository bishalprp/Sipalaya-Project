from django.shortcuts import render

# Create your views here.

# ---------------------------------------- back -------------------------------------------------

def course_details(request):
    return render(request,'back/course_details.html')

def degree_details(request):
    return render(request,'back/degree_details.html')

def school_details(request):
    return render(request,'back/school_details.html')

def skill_details(request):
    return render(request,'back/skill_details.html')

# ---------------------------------------------------------------------------------------------------