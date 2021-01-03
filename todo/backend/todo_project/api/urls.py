from django.urls import path

from .views import TodoListView, DetailTodo

urlpatterns = [

    path('', TodoListView.as_view(), name='api'),  # views.home

    path('<int:pk>/', DetailTodo.as_view(), name='detail-todo-api'),

]
