from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .models import User, Project, Tag, Task, Comment
from .serializers import UserSerializer, ProjectSerializer, TagSerializer, TaskSerializer, CommentSerializer, UserRegisterSerializer, LoginSerializer
from rest_framework.generics import CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class UserView(APIView):    
    """
    Show all registered users.
    """

    permission_classes = [IsAdminUser]

    def get(self, request):

        all_users = User.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserRegisterView(CreateAPIView):
    """
    Register a new user.
    """

    serializer_class = UserRegisterSerializer

class SessionLoginView(APIView):
    """
    Login user using Django session auth.
    """

    def get(self, request):
        """
        Return example login input for DRF browsable API.
        """
        serializer = LoginSerializer()
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LogoutView(APIView):
    """
    Logout the current user.
    """
    def get(self, request):
        logout(request)
        return Response({'message': 'Logout successfull!'}, status=status.HTTP_200_OK)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Basic CRUD operations for Project objects. Filters and order fields
    """

    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['name', 'description']

    def perform_create(self, serializer):
        """
        Save the currently logged user as an owner when creating a new project.
        """

        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        Filters all projects and return only those create by the current user.
        """

        return Project.objects.filter(owner=self.request.user)


class TagViewSet(viewsets.ModelViewSet):
    """
    Basic CRUD operations for Tag objects.
    """

    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    Basic CRUD operations for Task objects. Filter, search and order fields.
    """

    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline', 'project', 'tags']
    search_fields = ['title', 'description']
    ordering_fields = ['deadline', 'title']
    ordering = ['deadline']


class CommentViewSet(viewsets.ModelViewSet):
    """
    Basic CRUD operations for Comment objects.
    """

    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """
        Set the logged-in user as the author of the comment on creation.
        """

        serializer.save(user=self.request.user)

