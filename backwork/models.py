import re
from django.db import models
from subjects.models import Course,Type
from ckeditor.fields import RichTextField

# Create your models here.

class OfferedProgram(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    Coursename = models.CharField(max_length=250)


class CourseDetails(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='CourseDetails_image')
    Logo = models.ImageField(upload_to='CourseDetails_logo')
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=250, null=True)
    About = RichTextField(blank=True)
    # OfferedProgram = models.ForeignKey(OfferedProgram,on_delete=models.CASCADE)
    AdmissionGuidances = RichTextField(blank=True)
    Admissionlink = models.URLField()
    clzlink = models.URLField()
    Scholarship = RichTextField(blank=True)
    Location = models.CharField(max_length=250)
    video_link = models.URLField(blank=True)
    Type = models.ForeignKey(Type, on_delete=models.CASCADE ,null=True)

    def get_embed_video(self):
        if "youtubr.com" in self.video_link or "youtu.be" in self.video_link:
            return self.video_linkreplace("watch?v=","embed/")
        return None

    def __str__(self):
        return self.Name
