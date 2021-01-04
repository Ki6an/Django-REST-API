from rest_framework import generics, permissions

from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly  


class PostsListView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # <--  view level authentication 
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):
     
    permission_classes = (IsAuthorOrReadOnly,)  # <--  view level authentication 
    
    # allows access to the details page only if you are logged in.
    if permissions.IsAuthenticated:  
        permission_classes = (permissions.IsAuthenticated,)
   
    queryset = Post.objects.all()
    serializer_class = PostSerializer
