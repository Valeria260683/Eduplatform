from django.contrib import admin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import CustomUserManager
from .mixins import DateTimeMixin


class User(AbstractBaseUser, BaseUserManager, DateTimeMixin):
    first_name = models.CharField("first name", max_length=150, blank=True)
    last_name = models.CharField("last name", max_length=150, blank=True)
    email = models.EmailField("email address", unique=True)

    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)
    is_superuser = models.BooleanField("superuser status", default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "is_superuser"]

    def __str__(self):
        return f"{self.pk} - {self.email}"

    def get_full_name(self):
        def __str__(self):
            {self.first_name.capitalize()} - {self.last_name.capitalize()}

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Teacher(models.Model, DateTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.experience} xp"

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = "teachers"


class Student(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return f" {self.pk} - {self.rating} rating."

    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"


class Group(models.Model, DateTimeMixin):
    group_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student = models.ManyToManyField(Student, blank=True)
    course = models.ForeignKey(
        "testing_system.Course", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return f"{self.pk} {self.group_name}"

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"
