# Update `title` of a `Book` Instance

## Properties
- title

```
from bookshelf.models import Book

book = Book.objects.first()

book.title = "Nineteen Eighty-Four"
book.save()
```