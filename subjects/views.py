from django.shortcuts import render
from .models import Field,University,Course,Level,District,Affiliation,SchoolLevel,School,Degree,Skill
from django.core.paginator import Paginator


# Create your views here.

# -------------------------------------------- front ------------------------------------------

def courses(request):
    lev=Level.objects.all()
    dis=District.objects.all()
    fie=Field.objects.all()
    uni=University.objects.all()

# ...................... Paginator ..........................
    cour=Course.objects.all()
    courid=request.GET.get('')
    if courid:
        data=courses.objects.filter(Field=courid)
    else:
        data=Course.objects.all()
    paginator=Paginator(data,12)
    page_number=request.GET.get('page')
    num_p=paginator.get_page(page_number)
    total=num_p.paginator.num_pages
# .........................................................

    context={
        'lev':lev,
        'dis':dis,
        'fie':fie,
        'uni':uni,
        'sub':num_p,
        'cour':cour,
        'num':[n+1 for n in range(total)]
    }
    return render(request,'front/courses.html',context)

def degree(request):
    deg=Degree.objects.all()
    degid=request.GET.get('')
    if degid:
        degr=Degree.objects.filter(Field=degid)
    else:
        degr=Degree.objects.all()
    paginator=Paginator(degr,6)
    page_number=request.GET.get('page')
    num_set=paginator.get_page(page_number)
    total=num_set.paginator.num_pages

    fie=Field.objects.all()
    lev=Level.objects.all()

    context={
    'deg':deg,
    'fie':fie,
    'lev':lev,
    'dee':num_set,
    'num':[o+1 for o in range(total)]
    }
    return render(request,'front/degree.html',context)

def school(request):
    sch=School.objects.all()
    schid=request.GET.get('')
    if schid:
        scho=School.objects.filter(Field=schid)
    else:
        scho=School.objects.all()
    paginator=Paginator(scho,6)
    page_number=request.GET.get('page')
    num_s=paginator.get_page(page_number)
    total=num_s.paginator.num_pages

    fie=Field.objects.all()
    lev=Level.objects.all()
    dis=District.objects.all()
    aff=Affiliation.objects.all()

    context={
    'sch':sch,
    'fie':fie,
    'lev':lev,
    'dis':dis,
    'aff':aff,
    'scc':num_s,
    'num':[p+1 for p in range(total)]

    }
    return render(request,'front/school.html',context)

def skill(request):
    ski=Skill.objects.all()
    skiid=request.GET.get('')
    if skiid:
        skil=Skill.objects.filter(Field=skiid)
    else:
        skil=Skill.objects.all()
    paginator=Paginator(skil,8)
    page_number=request.GET.get('page')
    num_se=paginator.get_page(page_number)
    total=num_se.paginator.num_pages

    fie=Field.objects.all()
    lev=Level.objects.all()
    dis=District.objects.all()
    aff=Affiliation.objects.all()
    context={
    'ski':ski,
    'skk':num_se,
    'num':[q+1 for q in range(total)]

    }
    return render(request,'front/skill.html',context)

# -----------------------------------------------------------------------------------------------
