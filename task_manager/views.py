from django.http import HttpResponse
from django.views import View


class HomePageView(TemplateView):
    template_name = "home.html"
