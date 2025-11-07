#!/usr/bin/python3

from models import Book, Library

# Query all books by a specific author
books_by_Richard = Book.objects.filter(author="Richard")

# List all books in a library.
library_name = "Central Library"
library_books = Library.objects.get(name=library_name).books.all()

#Retrieve the librarian for a library
librarian = Library.objects.filter(name=library_name).first().librarian
