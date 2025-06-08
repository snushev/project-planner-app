from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User, Project, Tag, Task, Comment
from .serializers import UserSerializer, ProjectSerializer, TagSerializer, TaskSerializer, CommentSerializer, UserRegisterSerializer, LoginSerializer
from rest_framework.generics import CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class UserView(APIView):    
    "Show all registered users."

    permission_classes = [IsAdminUser]

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

class LoginView(APIView):
    """Login user and return auth token."""
    
    def get(self, request):
        return Response(LoginSerializer().data)
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Project objects. Filters and order fields"""

    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        """Save the currently logged user as an owner when creating a new project."""

        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """Filters all projects and return only those create by the current user."""

        return Project.objects.filter(owner=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Tag objects."""

    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Task objects. Filter, search and order fields."""

    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline', 'project', 'tags']
    search_fields = ['title', 'description']
    ordering_fields = ['deadline', 'title']
    ordering = ['deadline']


class CommentViewSet(viewsets.ModelViewSet):
    """Basic CRUD operations for Comment objects."""

    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Set the logged-in user as the author of the comment on creation."""

        serializer.save(user=self.request.user)

