from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from converter.views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),
    path('convert/', include('converter.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
