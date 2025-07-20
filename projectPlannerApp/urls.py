from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserView, ProjectViewSet, TagViewSet, TaskViewSet, CommentViewSet, UserRegisterView, SessionLoginView, LogoutView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()


router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'comments', CommentViewSet, basename='comment')

schema_view = get_schema_view(
   openapi.Info(
      title="TaskHub API",
      default_version='v1',
      description="API for managing projects, tasks, tags and comments.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', SessionLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls