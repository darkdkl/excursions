from django.shortcuts import render, get_object_or_404
from .models import Place
from django.http import JsonResponse
from django.urls import reverse


def get_places(places):
    places_data = []
    for place in places:
        places_data.append({
                "type": "Feature",
                "geometry": {
                        "type": "Point",
                        "coordinates": [place.lng, place.lat]
                },
                "properties": {
                        "title": place.title,
                        "placeId": "moscow_legends",
                        "detailsUrl": reverse("place", args={place.id})
                }
        })
    return places_data


def index(request):
    context = {"places": {"type": "FeatureCollection",
                          "features": get_places(Place.objects.all())}
               }
    return render(request, 'places/index.html', context=context)


def get_place_details(place):
    details = {
            "title": place.title,
            "imgs": [image.image.url for image in place.imgs.all()],
            "description_short": place.short_description,
            "description_long": place.long_description,
            "coordinates": {
                    "lat": place.lat,
                    "lng": place.lng}
              }
    return details


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(get_place_details(place),
                        json_dumps_params={'ensure_ascii': False})
