# Generated by Django 4.2.9 on 2024-01-03 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dailytask_app', '0002_remove_dailytask_task_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTaskDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_description', models.TextField(max_length=50)),
                ('task_status', models.CharField(choices=[('pending', 'pending'), ('running', 'running'), ('completed', 'completed')], default='pending', max_length=50)),
                ('daily_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dailytask_app.dailytask')),
            ],
        ),
    ]
