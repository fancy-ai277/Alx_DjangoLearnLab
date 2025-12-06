from django.contrib import admin
from django.urls import path, include  # include is required to link app urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # THIS connects your app's urls
]

