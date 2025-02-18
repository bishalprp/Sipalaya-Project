from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages

from datetime import datetime
# Create your views here.

def private(request):
    return render(request,'private.html')

def terms(request):
    return render(request,'terms.html')

def help(request):
    return render(request,'help.html')

# ----------------------------------------------------------- for footer sendmail -----------------------------------------------
def basemail(request):
    subjects = "Dream Success"
    message = 'hello 12323' #render_to_string('basemail',{'first_name':first_name, "date":date})
    from_email = 'prajapatibishal57@gmail.com'
    reciption_list = ['bp23447@gmail.com']

    send_mail(subject=subjects, message=message, from_email=from_email, recipient_list=reciption_list, fail_silently=True)
    # messages.success(request,f'Hi {first_name} thankyou for providing your email')

    return render(request,'basemail.html')

# ---------------------------------------------------------------------------------------------------------------------------