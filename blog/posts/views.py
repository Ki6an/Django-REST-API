from django.views.generic import ListView
from .models import Post


# Create your views here.
class PostsListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
