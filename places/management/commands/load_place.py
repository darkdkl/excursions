from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from excursions.settings import BASE_DIR
from places.models import Place, Image
import requests
import json
import os
import uuid


class Command(BaseCommand):
    def get_file_content(self, urls):
        for url in urls:
            response = requests.get(url)
            if response.ok:
                yield response.content, url.rsplit(".")[-1]

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'json_data_to_load/')
        files_json = [file for file in os.listdir(path)
                      if file.endswith('.json')]
        for file in files_json:
            with open(os.path.join(path, file)) as json_file:
                place_info = json.load(json_file)
            place_imgs = place_info.pop('imgs')
            lng = place_info['coordinates'].get("lng")
            lat = place_info['coordinates'].get("lat")
            place_info["short_description"] = place_info.pop('description_short')
            place_info["long_description"] = place_info.pop('description_long')
            place_info.pop("coordinates")
            place, exists = Place.objects.get_or_create(**place_info,
                                                        lng=lng, lat=lat)
            for file, extension in self.get_file_content(place_imgs):
                image = Image.objects.create(place=place)
                filename = str(uuid.uuid4()) + '.' + extension
                image.image.save(filename, ContentFile(file), save=True)
        self.stdout.write(self.style.SUCCESS("Импорт завершен успешно"))
