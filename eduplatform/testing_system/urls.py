from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import (AnswerViewSet, ArticleViewSet, AttemptViewSet,
                        CourseContentAPIView, CourseTopicAPIView,
                        CourseViewSet, QuestionAnswerAPIView, QuestionViewSet,
                        TestQuestionAPIView, TestViewSet, TopicArticleAPIView,
                        TopicViewSet)

router = DefaultRouter()
router.register(r"course", CourseViewSet)
router.register(r"topic", TopicViewSet)
router.register(r"article", ArticleViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"answer", AnswerViewSet)
router.register(r"attempt", AttemptViewSet)
router.register(r"test", TestViewSet)  # Добавляем путь для списка тестов

urlpatterns = [
    path("", include(router.urls)),
    path(
        "course/<int:course_id>/topics",
        CourseTopicAPIView.as_view(),
        name="course_topics",
    ),
    path(
        "topic/<int:topic_id>/articles",
        TopicArticleAPIView.as_view(),
        name="topic_articles",
    ),
    path(
        "test/<int:test_id>/questions",
        TestQuestionAPIView.as_view(),
        name="test_questions",
    ),
    path(
        "question/<int:question_id>/answers",
        QuestionAnswerAPIView.as_view(),
        name="question_answers",
    ),
    path(
        "course/<int:course_id>/content",
        CourseContentAPIView.as_view(),
        name="course_content",
    ),
]
