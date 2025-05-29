from django.http import HttpResponse
from django.views import View


class home(View):
    def get(self, request):
        return HttpResponse("Привет, мир! Это главная страница.")
