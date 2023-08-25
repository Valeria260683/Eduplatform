from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import (CourseViewSet, TopicViewSet,
                        ArticleViewSet, TestViewSet,
                        QuestionViewSet, AnswerViewSet,
                        AttemptViewSet, CourseTopicAPIView,
                        TopicArticleAPIView, TestQuestionAPIView,
                        QuestionAnswerAPIView, CourseContentAPIView)

router = DefaultRouter()
router.register(r"course", CourseViewSet)
router.register(r"topic", TopicViewSet)
router.register(r"article", ArticleViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"answer", AnswerViewSet)
router.register(r"attempt", AttemptViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("course/<int:course_id>/topics", CourseTopicAPIView.as_view(), name="course_topics"),
    path("topic/<int:topic_id>/articles", TopicArticleAPIView.as_view(), name="topic_articles"),
    path("test/<int:test_id>/questions", TestQuestionAPIView.as_view(), name="test_questions"),
    path("question/<int:question_id>/answers", QuestionAnswerAPIView.as_view(), name="question_answers"),
    path("course/<int:course_id>/content", CourseContentAPIView.as_view(), name="course_content"),

]