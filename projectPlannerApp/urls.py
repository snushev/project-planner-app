from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserView, ProjectViewSet, TagViewSet, TaskViewSet, CommentViewSet, UserRegisterView
router = DefaultRouter()


router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('register/', UserRegisterView.as_view(), name='register')
] + router.urls