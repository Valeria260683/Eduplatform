from .models import User, Teacher, Student, Group


def create_user():
    user = User.objects.create_user(
        password="qwerty",
        first_name="Name_test", last_name="Surname_test",
        email="test@mail.ru")
    return user