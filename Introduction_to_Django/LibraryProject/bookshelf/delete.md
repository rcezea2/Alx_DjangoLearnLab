# Delete a `Book` Instance


```
from bookshelf.models import Book

book = Book.objects.first()

book.delete()
```