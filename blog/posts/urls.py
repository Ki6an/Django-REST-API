from django.urls import path

from .views import PostsListView

urlpatterns = [

    path('', PostsListView.as_view(), name='todo-home'),  # views.home

]
