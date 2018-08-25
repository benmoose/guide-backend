from django.http import HttpResponse
from django.views import View


class ListView(View):
    def get(self, request):
        return HttpResponse('Hello, world!')
