from rest_framework import serializers

from dailytask_app.models import DailyTask, DailyTaskDetails


class DailyTaskSerializer(serializers.ModelSerializer):
    """
        A viewset that provides default `create()`, `retrieve()`, `update()`,
        `partial_update()`, `destroy()` and `list()` actions.
    """
    #task_id = serializers.ReadOnlyField()

    class Meta:
        model = DailyTask
        fields = '__all__'




class DailyTaskDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = DailyTaskDetails
        fields = '__all__'





