# Generated by Django 2.2.7 on 2020-02-08 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Model_Relationship', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='Applicant_Name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='CompanyName',
            field=models.CharField(max_length=20),
        ),
    ]
