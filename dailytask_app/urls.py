from rest_framework import routers
from dailytask_app.views import DailyTaskView, DailyTaskDetailView, GetTaskIDUserNameClassView
from django.urls import path, include
from . import views


router = routers.DefaultRouter()
router.register(r'dailytask', DailyTaskView, basename='dailytask')
router.register(r'dailytaskdetails', DailyTaskDetailView, basename='dailytaskdetails')
urlpatterns = [
    path('', include(router.urls)),
    path('get_taskid_username_classview/', GetTaskIDUserNameClassView.as_view(), name='get_daily_user_details_class'),
    path('get_taskid_username_funview/', views.GetDailyUserDetailFunView, name='get_daily_user_detail_fun')
]