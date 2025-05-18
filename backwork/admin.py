from django.contrib import admin
from .models import CourseDetails, OfferedProgram
from django.utils.html import format_html

# Register your models here.


    
# @admin.register(CourseDetails)
admin.site.register(CourseDetails)
class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Course', 'OfferedProgram', 'Location',)
    list_filter = ('Course', 'OfferedProgram', 'Location',)
    search_fields = ('Name', 'Location',)
    readonly_fields = ('get_embed_video',)


@admin.register(OfferedProgram)
class OfferedProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'Coursename')
    search_fields = ('coursename',)

