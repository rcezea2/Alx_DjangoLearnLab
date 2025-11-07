from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Library, Book

# Create your views here.

def list_books(request):
    book_list = Book.objects.all()
    context = {
        "books": book_list
    }
    return render(request, template_name="relationship_app/list_books.html", status=200, context=context)

class LibraryDetail(ListView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_queryset(self):
        return Library.objects.first()
