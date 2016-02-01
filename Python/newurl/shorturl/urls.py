from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^shorturl/$', views.make_short, name='make_short'),
    url(r'^change/$', views.change, name='change'),
    url(r'^(?P<new_url>.*$)', views.original, name='original'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

