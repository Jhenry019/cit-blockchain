# Generated by Django 3.1.1 on 2020-11-02 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0005_auto_20201102_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrecord',
            name='bio',
            field=models.TextField(default='No bio'),
        ),
    ]