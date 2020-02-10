# Generated by Django 3.0.1 on 2020-02-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('Mobile_No', models.IntegerField()),
                ('Address', models.CharField(max_length=30)),
                ('pdf', models.FileField(upload_to='CV/pdfs/')),
            ],
        ),
    ]
