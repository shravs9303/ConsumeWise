from django.urls import path
from . import views  # Make sure this line is present
from .views import ImageUploadView  # Ensure this import is present

urlpatterns = [
    path('', views.home, name='home'),
    path('query/', views.query_view, name='query'),
    path('upload_image/', views.upload_image, name='upload_image'),  # Ensure this line is correct
    path('upload-image/', ImageUploadView.as_view(), name='upload_image'),
]
