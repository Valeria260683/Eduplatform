from rest_framework import permissions, mixins
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from itertools import chain
from django.http import HttpResponse


from .models import User, Teacher, Student, Group
from .serializers import UserSerializer, TeacherSerializer, StudentSerializer,\
GroupSerializer, TeacherStudentSerializer, RegisterSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class TeacherViewset(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]

class StudentViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]

class GroupViewset(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]

class GroupStudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        group = self.kwargs["id"]
        return Student.objects.filter(group=group)

class GroupMembersAPIView(ListAPIView):
    serializer_class = TeacherStudentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        group = self.kwargs["id"]
        students = Student.objects.filter(group=group)
        teacher = Teacher.objects.filter(group=group)
        members = list(chain(set(students), set(teacher)))
        return members

class RegisterUserViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(f"User {serializer.data['email']} created!", status=201)
