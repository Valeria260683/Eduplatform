from django.http import HttpResponse
from django.views import View


class UserListView(View):
    def get(self, request):
        # Ваш код для обработки GET-запроса
        return HttpResponse("Привет, это представление для списка пользователей!")

    def post(self, request):
        # Ваш код для обработки POST-запроса
        # Предположим, что создание нового пользователя успешно
        # Тогда возвращаем код ответа 201 (HTTP_201_CREATED)
        return HttpResponse(
            "Привет, это представление для создания нового пользователя!", status=201
        )
