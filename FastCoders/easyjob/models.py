from django.db import models

class EmpManager(models.Manager):
    pass


class Company(models.Model):
    cCompanyName=models.CharField(max_length=100)
    cVacantPost=models.CharField(max_length=100)
    cVacancyNumber=models.IntegerField()
    cEmail=models.EmailField(max_length=100)
    cMobile=models.IntegerField()
    cLocation=models.CharField(max_length=50)

    objects= EmpManager()

    class Meta:
        db_table="Company"  
