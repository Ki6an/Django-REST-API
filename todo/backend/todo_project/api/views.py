from rest_framework import generics

from todos.models import Todo
from .serializers import TodoSerializer


class TodoListView(generics.ListAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
