from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Project, Tag, Task, Comment
from .serializers import UserSerializer, ProjectSerializer, TagSerializer, TaskSerializer, CommentSerializer, UserRegisterSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.

class UserView(APIView):    
    "Show all registered users."

    def get(self, request):
        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# A basic APIView logic for register a new user.

# class UserRegisterView(APIView):

#     def post(self, request):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Later switched to GenericAPIView to have the automatic creation form

class UserRegisterView(CreateAPIView):
    """Register a new user."""

    serializer_class = UserRegisterSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Project objects."""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        """Save the currently logged user as an owner when creating a new project."""

        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """Filters all projects and return only those create by the current user."""

        return Project.objects.filter(owner=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Tag objects."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Task objects."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Comment objects."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Set the logged-in user as the author of the comment on creation."""

        serializer.save(user=self.request.user)

