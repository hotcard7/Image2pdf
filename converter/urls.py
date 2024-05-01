from django.urls import path
from .views import image_to_pdf

urlpatterns = [
    path('', image_to_pdf, name='convert_to_pdf'),
]
