from django.views.generic import ListView
from .models import Todo


# Create your views here.
class TodoListView(ListView):
    model = Todo
    template_name = 'todos/todo_list.html'