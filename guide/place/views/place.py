from guide.common.http import parse_body_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View

from ..data_models.place import Place
from ..interface.place import get_all_places


class ListView(View):
    def post(self, request):
        data = parse_body_to_dict(request.body)

        place = Place.safe_from_dict(data)
        if place is None:
            return HttpResponseBadRequest()

        db_place = place.to_db_model()
        db_place.save()
        return JsonResponse(place.to_dict(), status=201)

    def get(self, request):
        places = get_all_places()
        print(places)
        return JsonResponse({})
