from django import forms
from django.forms import modelformset_factory
from .models import Entrance, Question, Answer, Option


class EntranceForm(forms.ModelForm):
    class Meta:
        model = Entrance
        fields= ['title','description']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter entrance title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter entrance description'})
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter the question text'})
        }

# OptionFormSet = modelformset_factory(
#     option,
#     fields=('option_text'),
#     extra=4,
#     min_num=4,
#     max_num=4,
#     validate_min=True,
#     widgets={
#         'option_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter option text'}),
#     }
# )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
        widgets = {
            'answer_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the correct answer'})
        }
