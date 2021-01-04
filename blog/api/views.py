# '''
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from posts.models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostsListView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # <--  view level authentication
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DetailPost(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)  # <--  view level authentication

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


'''

# --------------------------------------------
#              with View-Set  
# --------------------------------------------
from django.contrib.auth import get_user_model
from rest_framework import viewsets   # <--- 

from posts.models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# '''
