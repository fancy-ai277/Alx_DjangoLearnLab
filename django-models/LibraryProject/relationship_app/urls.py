from django.urls import path
from .admin_view import admin_view  # import from admin_view.py

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
]

