from django.contrib import admin
from django.urls import path, include
from core.views import upload_image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # This should correctly include core's URL patterns
    path('upload_image/', upload_image, name='upload_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)