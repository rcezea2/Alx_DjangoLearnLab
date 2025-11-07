#!/usr/bin/python3

from models import Book, Library

# Query all books by a specific author
books_by_Richard = Book.objects.filter(author="Richard")

# List all books in a library.
library = Library.objects.get(name="library_name")
library_books = library.books.all()

#Retrieve the librarian for a library
librarian = Library.objects.filter(name="ibrary_name").first().librarian
