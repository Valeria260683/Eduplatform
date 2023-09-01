from django.urls import reverse
from mentorship.consts import (USER_DATA, create_article, create_course,
                               create_group, create_student, create_teacher,
                               create_topic, create_user)
from mentorship.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import ArticleSerializer, CourseSerializer, TopicSerializer

__all__ = {
    "CreateCourseTest",
    "ReadCourseTest",
    "UpdateCourseTest",
    "DeleteCourseTest",
    "CreateTopicTest",
    "ReadTopicTest",
    "UpdateTopicTest",
    "DeleteTopicTest",
    "CreateArticleTest",
    "ReadArticleTest",
    "UpdateArticleTest",
    "DeleteArticleTest",
}


class CreateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)

    def test_create_course(self):
        url = reverse("course-list")
        response = self.client.post(
            url,
            data={"course_name": "Test", "teacher": self.teacher.id, "price": 1500},
            format="json",
        )
        self.course = create_course(self.teacher)


class ReadCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_read_course_list(self):
        url = reverse("course-list")
        response = self.client.get(url)
        self.client.force_authenticate(self.user)

    def test_read_course_detail(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.get(url)
        self.client.force_authenticate(self.user)


class UpdateCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.data = CourseSerializer(self.course).data
        self.data.update({"course_name": "NewTestName"})

    def test_update_course(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.put(url, self.data, format="json")
        self.client.force_authenticate(self.user)


class DeleteCourseTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_delete_course(self):
        url = reverse("course-detail", args=[self.course.id])
        response = self.client.delete(url)
        self.client.force_authenticate(self.user)


class CreateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)

    def test_create_topic(self):
        url = reverse("topic-list")
        response = self.client.post(
            url,
            data={"name": "Test", "course": self.course.id, "content": "123456"},
            format="json",
        )
        self.client.force_authenticate(self.user)


class ReadTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_read_topic_list(self):
        url = reverse("topic-list")
        response = self.client.get(url)
        self.client.force_authenticate(self.user)

    def test_read_topic_detail(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.get(url)
        self.client.force_authenticate(self.user)


class UpdateTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.data = TopicSerializer(self.topic).data
        self.data.update({"name": "NewTestName"})

    def test_update_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.put(url, self.data, format="json")
        self.client.force_authenticate(self.user)


class DeleteTopicTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_delete_topic(self):
        url = reverse("topic-detail", args=[self.course.id])
        response = self.client.delete(url)
        self.client.force_authenticate(self.user)


class CreateArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_create_article(self):
        url = reverse("article-list")
        response = self.client.post(
            url,
            data={
                "title": "Test",
                "topic": self.topic.id,
                "teacher": self.teacher.id,
                "content": "123456",
            },
            format="json",
        )
        self.client.force_authenticate(self.user)


class ReadArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)

    def test_read_article_list(self):
        url = reverse("article-list")
        response = self.client.get(url)
        self.client.force_authenticate(self.user)

    def test_read_article_detail(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.get(url)
        self.client.force_authenticate(self.user)


class UpdateArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)
        self.data = ArticleSerializer(self.article).data
        self.data.update({"title": "NewArticleTitle"})

    def test_update_article(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.put(url, self.data, format="json")
        self.client.force_authenticate(self.user)


class DeleteArticleTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)
        self.article = create_article(teacher_id=self.teacher, topic_id=self.topic)

    def test_delete_article(self):
        url = reverse("article-detail", args=[self.article.id])
        response = self.client.delete(url)
        self.client.force_authenticate(self.user)


class CreateTestTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.teacher = create_teacher(self.user)
        self.course = create_course(self.teacher)
        self.topic = create_topic(self.course)

    def test_create_test(self):
        url = reverse("test-list")
        response = self.client.post(
            url,
            data={
                "title": "Test",
                "topic": self.topic.id,
                "teacher": self.teacher.id,
                "description": "123456",
                "is_open": False,
            },
            format="json",
        )
        self.client.force_authenticate(self.user)
