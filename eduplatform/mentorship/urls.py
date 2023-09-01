from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .endpoints import (GroupMembersAPIView, GroupStudentAPIView, GroupViewset,
                        RegisterUserViewSet, StudentViewset, TeacherViewset,
                        UserViewset)
from .views import UserListView

router = DefaultRouter()
router.register("user", UserViewset)
router.register("teacher", TeacherViewset)
router.register("student", StudentViewset)
router.register("group", GroupViewset)
router.register("register", RegisterUserViewSet, basename="user_register")

urlpatterns = [
    path("", include(router.urls)),
    path("group/<id>/students/", GroupStudentAPIView.as_view(), name="group_students"),
    path("group/<id>/members/", GroupMembersAPIView.as_view(), name="group_members"),
    path("users/", UserListView.as_view(), name="user-list"),
]
