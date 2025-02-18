from django.db import models
from subjects.models import Course
from django.contrib.auth.models import User


# Create your models here.

class Entrance(models.Model):
    course = models.ForeignKey(
        Course, related_name='entrance', on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    entrance = models.ForeignKey(
        Entrance, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.OneToOneField(
        Question, related_name='correct_answer', on_delete=models.CASCADE
    )    
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return f"Correct Answer for: {self.question.question_text}"
    
class Option(models.Model):
    question = models.ForeignKey(
        Question, related_name='option', on_delete=models.CASCADE
    )
    option_text = models.CharField(max_length=255)

    def __str__(self):
        return self.option_text

# ------------------------------------------------------------ student progress ------------------------------------------------------------------------------------    

class StudentProgress(models.Model):
    user = models.ForeignKey(
        User, related_name='student_progresses', on_delete=models.CASCADE
    )
    entrance = models.ForeignKey(
        Entrance, related_name='entrances', on_delete=models.CASCADE, default=''
    )
    question = models.ForeignKey(
        Question, related_name='attempt_question', on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user', 'question')

    def __str__(self):
        return f'Username: {self.user}'

class Overallprogress(models.Model):
    user = models.ForeignKey(
        User, related_name='overall_progress', on_delete=models.CASCADE
    )
    entrance = models.ForeignKey(
        Entrance,related_name='entrance', on_delete=models.CASCADE
    )
    total_question = models.PositiveIntegerField()
    score = models.PositiveIntegerField()

    def __str__(self):
        return f'Username: {self.user} score: {self.score}'
