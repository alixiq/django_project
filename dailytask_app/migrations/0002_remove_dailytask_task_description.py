# Generated by Django 4.2.9 on 2024-01-03 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dailytask_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailytask',
            name='task_description',
        ),
    ]