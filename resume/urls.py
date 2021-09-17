from django.conf import settings
from django.urls import path
from django.views.static import serve
from .views import home
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', home, name='home'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    
]
