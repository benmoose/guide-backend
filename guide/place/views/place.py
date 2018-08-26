from guide.common.http import parse_body_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View

from ..data_models.place import Place
from ..interface.place import get_all_places, persist_place


class ListView(View):
    def post(self, request):
        data = parse_body_to_dict(request.body)

        place = Place.safe_from_dict(data)
        if place is None:
            return HttpResponseBadRequest()

        saved_place = persist_place(place)
        return JsonResponse(saved_place.to_dict(), status=201)

    def get(self, request):
        places = get_all_places()
        return JsonResponse({})
