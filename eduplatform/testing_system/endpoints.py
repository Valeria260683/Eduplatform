from itertools import chain

from django.db.models import Subquery
from rest_framework import generics, permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Answer, Article, Attempt, Course, Question, Test, Topic
from .serializers import (AnswerSerializer, ArticleSerializer,
                          AttemptSerializer, CourseSerializer,
                          QuestionSerializer, TestSerializer,
                          TopicArticleSerializer, TopicSerializer)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAdminUser]


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAdminUser]


class AttemptViewSet(ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseTopicAPIView(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs["course_id"]
        course = Course.objects.get(pk=course_id)
        queryset = Topic.objects.filter(course=course)
        return queryset


class TopicArticleAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        topic_id = self.kwargs["topic_id"]
        topic = Topic.objects.get(pk=topic_id)
        queryset = Article.objects.filter(topic=topic)
        return queryset


class TestQuestionAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        test_id = self.kwargs["test_id"]
        test = Test.objects.get(pk=test_id)
        queryset = Question.objects.filter(test=test)
        return queryset


class QuestionAnswerAPIView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        question_id = self.kwargs["question_id"]
        question = Question.objects.get(pk=question_id)
        queryset = Answer.objects.filter(question=question)
        return queryset


class CourseContentAPIView(generics.ListAPIView):
    serializer_class = TopicArticleSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        course = self.kwargs["course_id"]
        topics = Topic.objects.filter(course=course)
        articles = Article.objects.filter(topic__in=Subquery(topics.values("pk")))
        content = list(chain(set(topics), set(articles)))
        return content
