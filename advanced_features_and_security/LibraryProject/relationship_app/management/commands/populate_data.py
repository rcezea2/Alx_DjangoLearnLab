from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian

class Command(BaseCommand):
    help = 'Populates the Author, Book, Library, and Librarian models with sample data'

    def handle(self, *args, **kwargs):
        # Create some authors
        author1 = Author.objects.create(name="J.K. Rowling")
        author2 = Author.objects.create(name="George R. R. Martin")

        self.stdout.write(self.style.SUCCESS(f"Created authors: {author1.name}, {author2.name}"))

        # Create some books and associate them with authors
        book1 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author1)
        book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
        book3 = Book.objects.create(title="A Game of Thrones", author=author2)
        book4 = Book.objects.create(title="A Clash of Kings", author=author2)

        self.stdout.write(self.style.SUCCESS(f"Created books: {book1.title}, {book2.title}, {book3.title}, {book4.title}"))

        # Create a library
        library = Library.objects.create(name="Central Library")

        self.stdout.write(self.style.SUCCESS(f"Created library: {library.name}"))

        # Add books to the library
        library.books.add(book1, book2, book3, book4)
        self.stdout.write(self.style.SUCCESS("Added books to the library"))

        # Create a librarian and associate with the library
        librarian = Librarian.objects.create(name="Alice Johnson", library=library)

        self.stdout.write(self.style.SUCCESS(f"Created librarian: {librarian.name} and assigned to {librarian.library.name}"))
