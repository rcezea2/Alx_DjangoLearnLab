# Retrieve a `Book` Instance

## Properties
- title
- author
- publication year

```
from bookshelf.models import Book

book = Book.objects.first()

print(book.title)
print(book.author)
print(book.publication_year)
```