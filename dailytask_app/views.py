from django.http import JsonResponse
from rest_framework import viewsets

from dailytask_app.models import DailyTask, DailyTaskDetails
from dailytask_app.seralizers import DailyTaskSerializer, DailyTaskDetailSerializer

from django.db import connection
from django.views import View


# Create your views here.
class DailyTaskView(viewsets.ModelViewSet):
    queryset = DailyTask.objects.all()
    serializer_class = DailyTaskSerializer


class DailyTaskDetailView(viewsets.ModelViewSet):
    queryset = DailyTaskDetails.objects.all()
    serializer_class = DailyTaskDetailSerializer


class GetTaskIDUserNameClassView(View):
    def get(self, request):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    '''SELECT dt.task_id as task_id, dt.user_name as name, dtd.task_description as description 
                    FROM dailytask_app_dailytask dt JOIN dailytask_app_dailytaskdetails dtd 
                    ON dt.task_id = dtd.task_id_id''')
                results = cursor.fetchall()
                your_data = [{'task_id': row[0], 'name': row[1], 'description': row[2]} for row in results]

            return JsonResponse(your_data, safe=False)
        except Exception as e:
            print(e)


def GetDailyUserDetailFunView(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                '''SELECT dt.task_id, dt.user_name, dtd.task_description 
                FROM dailytask_app_dailytask dt JOIN dailytask_app_dailytaskdetails dtd 
                ON dt.task_id = dtd.task_id_id''')
            results = cursor.fetchall()
            your_data = [{'task_id': row[0], 'name': row[1], 'description': row[2]} for row in results]
            return JsonResponse(your_data, safe=False)

    except Exception as e:
        print(e)
