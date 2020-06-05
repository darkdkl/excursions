from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    description_short = models.TextField(verbose_name="Краткое описание")
    description_long = models.TextField(verbose_name="Полное описание")
    lat = models.FloatField(max_length=100, verbose_name="Широта")
    lng = models.FloatField(max_length=100, verbose_name="Долгота")

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name="Изображение")
    place = models.ForeignKey(Place, related_name="imgs",
                              on_delete=models.CASCADE,
                              verbose_name="Место", )
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return f'(файл: {self.image.name}'

    @property
    def place_title(self):
        return self.id, self.place.title
