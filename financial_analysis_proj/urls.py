from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finertia.urls')),  # Include the finertia app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Add this line to include built-in auth URLs
]
