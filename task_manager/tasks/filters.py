import django_filters
from .models import Task
from django import forms
from task_manager.labels.models import Label


class TaskFilter(django_filters.FilterSet):

    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Метки'
    )

    my_tasks = django_filters.BooleanFilter(
        method='filter_my_tasks',
        widget=forms.CheckboxInput,
        label="Только свои задачи"
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
        labels = {
            'status': 'Статус',
            'executor': 'Исполнитель',
            'labels': 'Метка'
        }

    def filter_my_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
