#!/usr/bin/python3

from models import Book, Library, Author, Librarian

# Query all books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# List all books in a library.
library_name = "Central Library"
library_books = Library.objects.get(name=library_name).books.all()

#Retrieve the librarian for a library
librarian_name = "Alice Johnson"
librarian = Librarian.objects.get(library=librarian_name).library
