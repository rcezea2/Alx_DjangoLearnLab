from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# View to list books (Only viewable by those with can_view permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View to create a book (Only accessible to users with can_create permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Creating a new book directly from POST data (assuming title, author, published_date are provided in request.POST)
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            book = Book.objects.create(
                title=title,
                author=author,
                published_date=published_date
            )
            return redirect('book_list')
    return render(request, 'bookshelf/book_create.html')

# View to edit a book (Only accessible to users with can_edit permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        # Updating book details directly from POST data
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        if title and author and published_date:
            book.title = title
            book.author = author
            book.published_date = published_date
            book.save()
            return redirect('book_list')

    return render(request, 'bookshelf/book_edit.html', {'book': book})

# View to delete a book (Only accessible to users with can_delete permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')


def book_search(request):
    query = request.GET.get('q', '')  # Get search term from query params
    books = Book.objects.filter(title__icontains=query)  # Use ORM to safely filter books

    return render(request, 'bookshelf/book_list.html', {'books': books})
