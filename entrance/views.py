from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import *
# from .forms import QuestionForm, OptionFormSet, AnswerForm, EntranceForm
from subjects.models import Course
from .forms import EntranceForm

# Create your views here.

# --------------------------------------- entrance -------------------------------------------------------
def create_entrance(request,course_id):
    form = EntranceForm()

    course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        form = EntranceForm(request.POST)
        if form.is_valid():
            entrance = form.save(commit=False)
            entrance.course = course
            entrance.save()
            return redirect('course_details', id=course_id)
    


    context = {
        'form': form,
        'course': course,
    }
    return render(request,'entrance/create_entrance.html', context)

def update_entrance(request):
    entrance = get_object_or_404(Entrance, id=entrance_id)
    if request.method == 'POST':
        form = EntaranceForm(request.POST, instance=entrance)
        if form.is_valid():
            form.save()
            return redirect('course_details', id=entrance.course.id)

        else:
            form = EntranceForm(instance=entrance)

        context = {
            'form' : form
        }
    return render(request,'entrance/create_entrance.html', context=context)


def detele_entrance(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# --------------------------------------------------------------------------------------------------------
# --------------------------------------- question --------------------------------------------------------

def create_question(request):
    # Fetching data /fetching-meaning
    entrance = get_object_or_404(Entrance, id=entrance_id)
    question = Question.objects.filter(entrance=entrance).prefetch_related('options')

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        option_formset = OptionFormSet(request.POST)
        answer_form = AnswerForm(request.POST)

        if question_form.is_valid() and option_formset.is_valid() and answer_form.is_valid():
            question = question_form.save(commit=False)
            question.entrance = entrance
            question.save()

            option = option_formset.save(commit=False)
            for option in options:
                option.question = question
                option.save()

            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()
        
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        else:
            print(question_form.errors)
            print(option_formset.errors)
            print(answer_form.errors)

    else:
        question_form = QuestionForm()
        option_formset = option_formset(queryset=Option.objects.nono())
        answer_form = AnswerForm()

    context = {
        'entrance' : entrance,
        'question_form' : question_form,
        'option_formset' : option_formset,
        'answer_form' : answer_form,
        'questions' : questions,
    }

    return render(request,'entrance/create_question.html', context=context)

# --------------------------------------------------------------------------------------------------------

# ------------------------------------------ update ------------------------------------------------------

def update_question(request, entrance_id, question_id):
    entrance = get_object_or_404(Entrance, id=entrance_id)
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
# --------------------------------- Process from data --------------------------------------------------------
        question_form = QuestionForm(request.POST,instance=question)
        option_formset = OptionFormSet(
            request.POST, queryset=Option.objects.filter(question=question)
            )
        answer_form = AnswerForm(
            request.POSt, instance=question.correct_answer if question.correct_answer else None
        )

    if question_form.is_valid() and option_formset.is_valid() and answer_form.is_valid():
# ................................... Save the update question ..........................................................
        question = question_form.save()
        
# ................................... Save the update options ............................................................
        option_formset.save(commit=False)
        for option in options:
            option.question = question
            option.save()

# ......................................save the update answer ........................................................
        if answer_form.cleaned_data.get('answer_text'):
            answer = answer_form.save(commit=False)
            answer.question = question
            answer.save()

        return redirect('create_question', entrance_id = entrance_id)
    
    else:
# .................................. Initialize forms for Get request ..............................................
        question_form = QuestionForm(instance=question)
        option_formset = OptionFormSet(
            queryset = Option.objects.filter(question=question)
        )
        answer_form = AnswerForm(
            instance=question.correct_question if question.correct_answer else None
        )

        context = {
            'entrance' : entrance,
            'question_form' : question_form,
            'option_formset' : option_formset,
            'answer_form' : answer_form,
        }
        
    return render(request,'entrance/update_question.html')

# ---------------------------------------------------------------------------------------------------------

# ----------------------------------------- delete --------------------------------------------------------


def delete_question(request, quiz_id, question_id):
    question = get_object_or_404(Question, id=question_id, quiz_id=quiz_id)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question.delete()
    return redirect('create_question', quiz_id=quiz.id)

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------- Entrance student ------------------------------------------

def show_entrance(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    entrance = Entrance.objects.filter(course=course)
    context = {
        'course' : course,
        'entrance' : entrance,
    }
    return render(request,'entrance/entrance_stu/show_entrance', context=context)

def show_entrance_question(request):
    entrance = get_object_or_404(Entrance, id=entrance_id)
    question = Question.objects.filter(quiz=quiz).prefetch_related('options')

# ............................. Organize options by their related questions .....................................

    question_with_options = []
    for question in questions:
        options = question.options.all()
        question_with_options.append({
            'question' : question,
            'options' : options,
        })

# ..................................................... entrance ...................................................

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                try:
                    selected_option = Option.objects.get(id=selected_option_id)
                    is_correct = Answer.objects.filter(
                        question=question, answer_text=selected_option.option_text
                    ).exists()
                    if is_correct:
                        if not StudentProgress.objects.filter(
                            user=request.user, entrance=entrance, question=question
                        ).exists():
                            student_progress = StudentProgress(
                                user=request.user, entrance=entrance, question=question
                            )
                            student_progress.save()
                            score +=1
                            print('correct')
                            print(score)
                        else:
                            score +=1
                            print('correct')
                            print(score)
                except Option.DoesNotExist:
                        print(f'Option with ID {
                            selected_option_id} does not exist.')
# .............................. Stort the score and entrance ID in session ..........................................
        request.session['score'] = score
        request.session['quiz_id'] = quiz_id
        return redirect('show_result')

    context = {
        'entrance' : entrance,
        'question_with_options' : question_with_options,
    }

    return render(request,'entrance/entrance_stu/show_entrance_question.html', context=context)

def show_result(request):
    score = request.session.get('score', 0)
    entrance_id = request.session.get('entrance_id')

    entrance = get_object_or_404(Entrance, id=entrance_id)
    total_question = entrance.question.count()
    incorrect_answers = total_question - score
    questions = Question.objects.filter(entrance=entrance)

# .............................. create or update overallprogress record ...................................................
    OverallProgress.objects.update_or_create(
        user= request.user,
        entrance= entrance,
        defaults = {
            'total_questions' : total_question,
            'score' : score,
        }
    )

#  ..................... Clean up session .........................................................................
    request.session.pop('score',None)
    request.session.pop('entrance_id', None)

    context = {
        'score' : score,
        'entrance' : entrance,
        'total_question' : total_question,
        'incorrect_answers' : incorrect_answers,
        'questions' : questions,
    }

    return render(request,'entrance/entrance_stu/result_entrance.html')

# ------------------------------------------------------------------------------------------------------------