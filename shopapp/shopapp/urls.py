from django.contrib import admin
from django.urls import include, path
from shopapp import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mymain.urls')),
    path('catalog/', include('goods.urls', namespace='catalog')),

]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)