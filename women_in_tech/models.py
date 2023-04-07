from django.db import models

# Create your models here.


class Technological_skills(models.Model):
    ID= models.AutoField(primary_key=True)
    skill = models.CharField(max_length=254, null=True, blank=True)
    def __str__(self):
        return str(self.skill)

class Mentor(models.Model):
    ID= models.AutoField(primary_key=True)
    mentor_name = models.CharField(max_length=254, null=True, blank=True)
    mentor_email= models.EmailField(max_length=254, unique=True)
    skills=models.ForeignKey("Technological_skills", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.mentor_name)

class Traning_module(models.Model):
    ID= models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=254, null=True, blank=True)
    #mentor_email= models.EmailField(max_length=254, unique=True)
    skills=models.ForeignKey("Technological_skills", on_delete=models.CASCADE)
    def __str__(self):
        return str(self.book_name)