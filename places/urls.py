from django.urls import path
import places.views as views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('', views.index, name='index'),
               path('place/<int:place_id>/', views.place,name="place"),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)