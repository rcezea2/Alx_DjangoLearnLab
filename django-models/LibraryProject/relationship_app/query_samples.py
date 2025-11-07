#!/usr/bin/python3

from models import Book, Library, Author

# Query all books by a specific author
author_name = "J.K. Rowling"
books_by_Richard = Author.objects.get(name=author_name).books.all()

# List all books in a library.
library_name = "Central Library"
library_books = Library.objects.get(name=library_name).books.all()

#Retrieve the librarian for a library
librarian = Library.objects.filter(name=library_name).first().librarian
