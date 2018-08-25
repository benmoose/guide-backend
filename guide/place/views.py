import json

from guide.common.http import parse_body_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View

from .data_models.place import Place


class ListView(View):
    def post(self, request):
        data = parse_body_to_dict(request.body)

        place = Place.safe_from_dict(data)
        if place is None:
            return HttpResponseBadRequest()

        db_place = place.to_db_model()
        db_place.save()
        return JsonResponse(place.to_dict())

    def get(self, request):
        return JsonResponse(dict(message='hello, world!'))
