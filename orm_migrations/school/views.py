from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    students = Student.objects.all().order_by(ordering).prefetch_related('teachers')

    context = {
        'object_list': students
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)
