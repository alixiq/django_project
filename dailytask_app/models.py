from django.db import models


# Create your models here.


class DailyTask(models.Model):
    task_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=50)
    task_title = models.CharField(max_length=50)
    created_date = models.DateField()


class DailyTaskDetails(models.Model):
    task_id = models.ForeignKey(DailyTask, on_delete=models.CASCADE)
    task_description = models.TextField(max_length=50, default=None)
    task_status = models.CharField(max_length=50,
                                   choices=[('pending', 'pending'), ('running', 'running'), ('completed', 'completed')],
                                   default='pending')