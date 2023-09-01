from django.urls import reverse
from mentorship.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .consts import (USER_DATA, create_course, create_group, create_student,
                     create_teacher, create_user)
from .serializers import (GroupSerializer, StudentSerializer,
                          TeacherSerializer, UserSerializer)

__all__ = {
    "CreateUserTest",
    "ReadUserTest",
    "UpdateUserTest",
    "DeleteUserTest",
    "CreateTeacherTest",
    "ReadTeacherTest",
    "UpdateTeacherTest",
    "DeleteTeacherTest",
    "CreateStudentTest",
    "ReadStudentTest",
    "UpdateStudentTest",
    "DeleteStudentTest",
    "CreateGroupTest",
    "ReadGroupTest",
    "UpdateGroupTest",
    "DeleteGroupTest",
}


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        response = self.client.post(url, data=USER_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        email = "admin@mail.ru"
        password = "qwerty"
        extra_fields = {"first_name": "admin", "last_name": "admin"}
        self.user = User.objects.create_user(
            email=email, password=password, **extra_fields
        )
        self.client.force_authenticate(self.user)

    def test_read_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.client.force_authenticate(self.user)

    def test_read_user_detail(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.client.force_authenticate(self.user)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.data = UserSerializer(self.user).data
        self.data.update({"first_name": "newName_test"})

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.put(url, self.data, format="json")
        self.client.force_authenticate(self.user)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.client.force_authenticate(self.user)


class CreateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_create_user(self):
        url = reverse("teacher-list")
        response = self.client.post(
            url, data={"experience": 12, "user": self.user.id}, format="json"
        )
        self.client.force_authenticate(self.user)


class ReadTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_read_teacher_list(self):
        url = reverse("teacher-list")
        response = self.client.get(url)
        self.client.force_authenticate(self.user)

    def test_read_teacher_detail(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.get(url)
        self.client.force_authenticate(self.user)


class UpdateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.data = TeacherSerializer(self.teacher).data
        self.data.update({"experience": 20})

    def test_update_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.put(url, self.data, format="json")
        self.client.force_authenticate(self.user)


class DeleteTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_delete_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.delete(url)
        self.client.force_authenticate(self.user)


class CreateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_create_student(self):
        url = reverse("student-list")
        response = self.client.post(
            url, data={"age": 22, "user": self.user.id, "rating": 85.30}, format="json"
        )
        self.client.force_authenticate(self.user)


class ReadStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_read_student_list(self):
        url = reverse("student-list")
        response = self.client.get(url)
        self.client.force_authenticate(self.user)

    def test_read_student_detail(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.get(url)
        self.client.force_authenticate(self.user)


class UpdateStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)
        self.data = StudentSerializer(self.student).data
        self.data.update({"age": 27})

    def test_update_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.put(url, self.data, format="json")
        self.client.force_authenticate(self.user)


class DeleteStudentTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.student = create_student(self.user)

    def test_delete_student(self):
        url = reverse("student-detail", args=[self.student.id])
        response = self.client.delete(url)
        self.client.force_authenticate(self.user)


class CreateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)

    def test_create_group(self):
        url = reverse("group-list")
        response = self.client.post(
            url,
            data={
                "group_name": "Test",
                "teacher": self.teacher.id,
                "student": [self.student.id],
                "course": self.course.id,
            },
            format="json",
        )
        self.client.force_authenticate(self.user)


class ReadGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(
            teacher_id=self.teacher, student_id=self.student, course_id=self.course
        )

    def test_read_group_list(self):
        url = reverse("group-list")
        response = self.client.get(url)
        self.client.force_authenticate(self.user)

    def test_read_group_detail(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.get(url)
        self.client.force_authenticate(self.user)


class UpdateGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(
            teacher_id=self.teacher, student_id=self.student, course_id=self.course
        )
        self.data = GroupSerializer(self.group).data
        self.data.update({"group_name": "newName"})

    def test_update_group(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.put(url, self.data, format="json")
        self.client.force_authenticate(self.user)


class DeleteGroupTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.student = create_student(self.user)
        self.course = create_course(self.teacher)
        self.group = create_group(
            teacher_id=self.teacher, course_id=self.course, student_id=self.student
        )

    def test_delete_group(self):
        url = reverse("group-detail", args=[self.group.id])
        response = self.client.delete(url)
        self.client.force_authenticate(self.user)
