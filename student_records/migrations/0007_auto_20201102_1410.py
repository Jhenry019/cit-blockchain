# Generated by Django 3.1.1 on 2020-11-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_records', '0006_studentrecord_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecord',
            name='bio',
            field=models.TextField(default='Enter a bio for <django.db.models.fields.CharField>'),
        ),
    ]