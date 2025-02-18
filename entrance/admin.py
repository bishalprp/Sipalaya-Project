from django.contrib import admin
from .models import *
# Register your models here.

class OptionInline(admin.TabularInline):
    model = Option
    extra = 4
    min_num = 4
    max_num = 4

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1
    min_num = 1
    max_num = 1

@admin.register(Entrance)
class EntranceAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'course', 'title', 'description', 'created_at', 'update_at'
    ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'entrance', 'question_text']
    search_fields = ['question_text', 'entrance_title']
    list_filter = ['entrance']
    inlines = [OptionInline, AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'answer_text']

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'option_text']
    list_filter = ['question']
    search_fields = ['option_text', 'question_text']
    list_select_related = ['question']

    def question(self, obj):
        return obj.question.text

    question.admin_order_field = 'question_text'
    question.short_description = 'Question'

@admin.register(StudentProgress)
class StudentProgressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'entrance', 'question']


@admin.register(Overallprogress)
class OverallProgressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'score']