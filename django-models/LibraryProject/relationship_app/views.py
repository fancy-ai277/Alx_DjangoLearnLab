from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Function-based view
def book_list_view(request):
    books = Book.objects.all()
    
    # Create a simple text list
    output = ""
    for book in books:
        output += f"{book.title} by {book.author.name}\n"
    
    return HttpResponse(output, content_type="text/plain")

