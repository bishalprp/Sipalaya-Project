from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from subjects.models import Course


from datetime import datetime
date=datetime.now()

# Create your views here.

# ======================================= footer part ==============================================================

def index(request):
    cour=Course.objects.all()
    courid=request.GET.get('')
    if courid:
        data=courses.objects.filter(Field=courid)
    else:
        data=Course.objects.all()
    paginator=Paginator(data,3)
    page_number=request.GET.get('page')
    num_p=paginator.get_page(page_number)
    total=num_p.paginator.num_pages



    context={
    'sub':num_p,
    'cour':cour,
    'num':[n+1 for n in range(total)],
    }

    return render(request,'footer/index.html',context)

def about(request):
    return render(request,'footer/about.html')

def contact(request):
    if request.method == "POST":
            
        subject="Dream Success"
        message= render_to_string('msg/contactmsg.html',{'name':name, "date":date}) 
        from_email='prajapatibishal57@gmail.com'
        reciption_list=[email]

        send_mail(subject=subject,message=message,from_email=from_email,recipient_list=reciption_list,fail_silently=True)
        messages.success(request,f"Hi {name} Your message has been successfully submit ")

    return render(request,'footer/contact.html')


def team(request):
    return render(request,'footer/team.html')

def testimonial(request):
    return render(request,'footer/testimonial.html')

# ================================================================================================================

