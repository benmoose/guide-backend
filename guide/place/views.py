import json

from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View

from .data_models.place import Place


class ListView(View):
    def post(self, request):
        data = json.loads(request.body)
        place = Place.safe_from_dict(data)

        if place is None:
            return HttpResponseBadRequest()

        return JsonResponse(place.to_dict())

    def get(self, request):
        return JsonResponse(dict(message='hello, world!'))
