import re
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# ------------------------------------------------------------ Front ------------------------------------------------------------------------------
class Field(models.Model):
    title=models.CharField(max_length=150)
    def __str__(self):
        return self.title
    
class District(models.Model):
    title=models.CharField(max_length=150,null=True)
    number=models.IntegerField(null=True)
    def __str__(self):
        return self.title

class Level(models.Model):
    title=models.CharField(max_length=150)
    number=models.IntegerField(null=True)
    def __str__(self):
        return self.title

class University(models.Model):
    title=models.CharField(max_length=150)
    number=models.IntegerField(null=True)
    def __str__(self):
        return self.title

class Course(models.Model):
    Name=models.CharField(max_length=150)
    Field=models.ForeignKey(Field, on_delete=models.CASCADE)
    Uinversity=models.ForeignKey(University, on_delete=models.CASCADE)
    Location=models.CharField(max_length=200,null=True)
    District=models.ForeignKey(District, on_delete=models.CASCADE,null=True)
    Level=models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    # Type=models.CharField(max_length=100, null=True)
    Image=models.ImageField(upload_to='Course_image')    
    Image2=models.ImageField(upload_to='Course_image')    
    Description=RichTextField(blank=True)
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

class Type(models.Model):
    title=models.CharField(max_length=200)
    number=models.IntegerField()
    def __str__(self):
        return self.title
    

class Affiliation(models.Model):
    title=models.CharField(max_length=250)
    number=models.IntegerField()
    def __str__(self):
        return self.title    

class SchoolLevel(models.Model):
    title=models.CharField(max_length=200)
    number=models.IntegerField()
    def __str__(self):
        return self.title    

class School(models.Model):
    Name=models.CharField(max_length=200)
    District=models.ForeignKey(District, on_delete=models.CASCADE)
    Location=models.CharField(max_length=200)
    Type=models.ForeignKey(Type, on_delete=models.CASCADE)
    Affiliation=models.CharField(max_length=250)
    SchoolLevel=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='School_image')
    Description=RichTextField(blank=True)
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
    
class Degree(models.Model):
    Name=models.CharField(max_length=250)
    Level=models.ForeignKey(Level, on_delete=models.CASCADE)
    Field=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='Degree_image')
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Skill(models.Model):
    Name=models.CharField(max_length=250)
    Duration=models.CharField(max_length=200)
    Image=models.ImageField(upload_to='Skill_image')
    
# -------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------- back ------------------------------------------------------------------------

# class Course_Details(models.Model):
#     Name=models.CharField(max_length=150)
#     Image1=models.ImageField(upload_to='Course_Details_image')
#     Logo=models.ImageField(upload_to='Course_Details_image')
#     Course_About=RichTextField(blank=True)


# ------------------------------------------------------------------------------------------------------------------------------------------------