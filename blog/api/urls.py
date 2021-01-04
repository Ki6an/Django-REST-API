# '''
from django.urls import path
from .views import PostsListView, DetailPost,  UserList, UserDetail
from rest_framework.schemas import get_schema_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# for api docs
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="A sample API for learning DRF",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="hello@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [

    path('', PostsListView.as_view(), name='posts-home'),  # views.home

    path('<int:pk>/', DetailPost.as_view(), name='detail-posts-api'),

    path('users/', UserList.as_view()),

    path('users/<int:pk>/', UserDetail.as_view()),



    # @ http://127.0.0.1:8000/api/v1/openapi/
    # path('openapi/', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …"
    # ), name='openapi-schema'),



    # api docs
    # @ http://127.0.0.1:8000/api/v1/swagger/
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),


    # @ http://127.0.0.1:8000/api/v1/redoc/#operation/v1_users_create
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),


]


'''

# ----------------------------------------
#                Routers
# ----------------------------------------

from django.urls import path
from rest_framework.routers import SimpleRouter # <--
from .views import UserViewSet, PostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')
urlpatterns = router.urls

'''

# Viewsets and routers are a powerful abstraction that reduce the amount of code we need to write
