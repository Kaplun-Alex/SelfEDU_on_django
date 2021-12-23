from django.urls import path, re_path
from sample.views import *

urlpatterns = [
    path('', index, name="home"),
    path('cats/<int:catid>/', categories),
    path('api/', apihelp),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]


