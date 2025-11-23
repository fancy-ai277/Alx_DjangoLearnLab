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

from .member_view import member_view  # import Member view

urlpatterns = [
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),  # Member URL
]
