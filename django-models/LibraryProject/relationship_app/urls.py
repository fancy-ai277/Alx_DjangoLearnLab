from django.urls import path
from .admin_view import admin_view  # import from admin_view.py

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
]

from .librarian_view import librarian_view  # import the Librarian view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),  # Librarian URL
]
