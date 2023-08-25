from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from .endpoints import UserViewset, TeacherViewset, StudentViewset, GroupViewset, GroupStudentAPIView, \
GroupMembersAPIView, RegisterUserViewSet


router = DefaultRouter()
router.register("user", UserViewset)
router.register("teacher", TeacherViewset)
router.register("student", StudentViewset)
router.register("group", GroupViewset)
router.register("register", RegisterUserViewSet, basename='user_register')

urlpatterns = [
    path("", include(router.urls)),
    path("group/<id>/students/", GroupStudentAPIView.as_view(), name="group_students"),
    path("group/<id>/members/", GroupMembersAPIView.as_view(), name="group_members")

]

