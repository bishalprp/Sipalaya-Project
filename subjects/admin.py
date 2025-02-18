from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Field,District,Level,University,Course,Type,Affiliation,SchoolLevel,School,Degree,Skill])

admin.site.site_header="Dream Success"
