from django.urls import path
from .views import TaskListCreateView,update_task_view
urlpatterns = [
    path('',TaskListCreateView.as_view(),name='task_list' ),
    path('update/<int:pk>/',update_task_view,name='update_task' ),
]
