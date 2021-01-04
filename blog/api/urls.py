from django.urls import path

from .views import PostsListView, DetailPost

urlpatterns = [

    path('', PostsListView.as_view(), name='posts-home'),  # views.home

    path('<int:pk>/', DetailPost.as_view(), name='detail-posts-api'),

]
