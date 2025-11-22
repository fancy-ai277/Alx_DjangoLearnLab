```python
from bookshelf.models import Book

# Retrieve a single book
book = Book.objects.get(title="1984")
book

# Retrieve all books
books = Book.objects.all()
books


