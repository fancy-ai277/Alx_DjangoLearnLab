from django.shortcuts import render
from .models import Book  # leave this as-is

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView  # <-- corrected import
from .models import Library  # <-- make sure Library is imported

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

