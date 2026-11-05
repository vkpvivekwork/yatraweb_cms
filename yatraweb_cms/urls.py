from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/packages/',    include('packages.urls')),
    path('api/bookings/',    include('bookings.urls')),
    path('api/travelstory/', include('travelstory.urls')),
    path('api/gallery/',     include('gallery.urls')),
    path('api/config/',      include('siteconfig.urls')),
    path('api/articles/',    include('articles.urls')),
    path('api/ghats/',       include('ghats.urls')),
    path('api/festivals/',   include('festivals.urls')),
]
