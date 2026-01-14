from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Simple home page view
def home(request):
    return JsonResponse({"message": "Welcome to Social Media API!"})

urlpatterns = [
    path('', home),  # Root URL
    path('admin/', admin.site.urls),  # Admin panel
    path('api/', include('accounts.urls')),  # Accounts app endpoints
    path('api/', include('posts.urls')),     # Posts app endpoints
]
