from django.shortcuts import render
import base64
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json  # Import json
import re  # Import re
from django.views import View  # Import the View class
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'core/home.html')

def query_view(request):
    if request.method == "POST":
        query = request.POST.get('query')
        return render(request, 'core/query.html', {'query': query})

# Disable CSRF protection for development (do NOT use in production)
  # Add this decorator if you're not using CSRF tokens in development
class ImageUploadView(View):
     # Disable CSRF protection for development (do NOT use in production)
    def post(self, request):
        data = json.loads(request.body)
        image_data = data['image']
        
        # Decode the image data
        image_data = re.sub('^data:image/.+;base64,', '', image_data)
        image_data = base64.b64decode(image_data)

        # Save the image
        with open('uploaded_image.png', 'wb') as f:
            f.write(image_data)

        return JsonResponse({'message': 'Image uploaded successfully'})
    
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        return HttpResponse(f"Uploaded: {filename}")
    return HttpResponse("Error uploading image!")