from testing_system.models import Article, Course, Topic

from .annotations import (ArticleAnnotation, CourseAnnotation, GroupAnnotation,
                          StudentAnnotation, TeacherAnnotation,
                          TopicAnnotation, UserAnnotation)
from .models import Group, Student, Teacher, User

USER_DATA = {
    "password": "qwerty",
    "first_name": "Name_test",
    "last_name": "Surname_test",
    "email": "test@mail.ru",
}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(
        password="qwerty",
        first_name="Name_test",
        last_name="Surname_test",
        email="test@mail.ru",
    )
    return user


def create_teacher(user_id) -> TeacherAnnotation:
    teacher = Teacher.objects.create(experience=10, user=user_id)
    return teacher


def create_student(user_id) -> StudentAnnotation:
    student = Student.objects.create(age=20, rating=50.55, user=user_id)
    return student


def create_course(teacher_id) -> CourseAnnotation:
    course = Course.objects.create(name="Test", teacher=teacher_id, price=1000)
    return course


def create_group(teacher_id, student_id, course_id) -> GroupAnnotation:
    group = Group.objects.create(
        group_name="Test", teacher=teacher_id, course=course_id
    )
    group.student.set([student_id])
    return group


def create_topic(course_id) -> TopicAnnotation:
    topic = Topic.objects.create(name="Test", course=course_id, content="123456")
    return topic


def create_article(teacher_id, topic_id) -> ArticleAnnotation:
    article = Article.objects.create(
        title="Test", teacher=teacher_id, topic=topic_id, content="123456"
    )
    return article
