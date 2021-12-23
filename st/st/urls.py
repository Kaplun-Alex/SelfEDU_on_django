from django.contrib import admin
from django.urls import path, include
from sample.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', include('sample.urls'))
]

handler404 = pageNotFound
