from django.db import models

# Create your models here.

class profileinfo(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    contact_number = models.CharField(max_length=13)
    description = models.CharField(max_length=300)
    degree = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    github_nick = models.CharField(max_length=100,null=True,blank=True)

    

class profiles(models.Model):
    profile_name = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    types = models.CharField(max_length=10,choices=(('Misc','Misc'),('Research','Research'),('Developer','Developer')),default='Developer',null=True,blank=True)
    importance = models.IntegerField()

class education(models.Model):
    degree = models.CharField(max_length=100)
    year_started = models.CharField(max_length=10,blank=True,null=True)
    year_ended = models.CharField(max_length=20)
    institute = models.CharField(max_length=100)
    cgpa = models.CharField(max_length=10)

class work_experience(models.Model):
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    start = models.CharField(max_length=20)
    end = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=200,null=True,blank=True)
    importance = models.CharField(max_length=200)
 
class publications(models.Model):
    headline = models.CharField(max_length=200)
    conference = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    importance = models.IntegerField(default=5)

class projects(models.Model):
    name = models.CharField(max_length=200)
    advisor = models.CharField(max_length=200,null=True,blank=True)
    importance = models.IntegerField()
    description = models.CharField(max_length=200,null=True,blank=True)
    link = models.CharField(max_length=200,null=True,blank=True)
    start_date = models.CharField(max_length=40)
    end_date = models.CharField(max_length=40)
    types = models.CharField(max_length=20,choices=(('Misc','Misc'),('Research','Research'),('Developer','Developer')),default='Developer',null=True,blank=True)
    
class skills(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()
    importance = models.IntegerField()
    types = models.CharField(max_length=10)

class achievements(models.Model):
    achievement = models.CharField(max_length=100)
    importance = models.IntegerField()

class cocurricular(models.Model):
    activity = models.CharField(max_length=100)
    importance = models.IntegerField()

