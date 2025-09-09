from django.urls import path
from .views import *
urlpatterns = [
    path('add-task/',addTask.as_view()),
    path('get-task/',retrieveTasks.as_view()),
    path('update-task/',addTask.as_view()),
    path('delete-task/',deleteTask.as_view()),

    # path('retrieve-amount/<int:amt>',accountview),


]