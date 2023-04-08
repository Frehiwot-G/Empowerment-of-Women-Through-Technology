from django.db import models

# Create your models here.
class Avaliable_jobs(models.Model):
    CATEGORY=(
        ('full time','full time'),
        ('part time','part time'),
    )
    ID= models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=254, null=True, blank=True)
    job_description = models.TextField(max_length=254, null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    job_type = models.CharField(max_length=254, null=True, blank=True, choices=CATEGORY)
    salary=models.IntegerField()
    kind_of_support = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return str(self.skill)