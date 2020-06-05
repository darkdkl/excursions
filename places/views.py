from django.shortcuts import render, get_object_or_404
from .models import Place
from django.http import JsonResponse
from django.urls import reverse


def get_places(obj):
    places = []
    for place in obj:
        places.append({
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
    return places


def index(request):
    context = {"places": {
        "type": "FeatureCollection",
        "features": get_places(Place.objects.all())
                        }
                }
    return render(request, 'places/index.html', context=context)


def get_place_details(obj):
    details = {
        "title": obj.title,
        "imgs": [image.image.url for image in obj.imgs.all()],
        "description_short": obj.description_short,
        "description_long": obj.description_long,
        "coordinates": {
            "lat": obj.lat,
            "lng": obj.lng}
                }
    return details


def place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return JsonResponse(get_place_details(place),
                        json_dumps_params={'ensure_ascii': False})
