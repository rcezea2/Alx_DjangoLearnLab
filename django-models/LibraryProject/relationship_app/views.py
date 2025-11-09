from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth import login, logout

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

# class Login(LoginView):
#     form_class = AuthenticationForm
#     template_name = "relationship_app/login.html"
#     # next_page = "https://www.google.com"
#     next_page = "dashboard"

# class Logout(LogoutView):
#     template_name = "relationship_app/logout.html"

class RegisterView(CreateView):
    form_class = UserCreationForm() # brackets to pass checks
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy('login')

@login_required()
def home(request):
    return render(request, "relationship_app/home.html")

def register(request):
    pass

def admin_view(request):
    if request.user.profile.role != "admin":
        return HttpResponseForbidden("Access denied.")
    return render(request, "relationship_app/admin_view.html")

def librarian_view(request):
    if request.user.profile.role != "librarian":
        return HttpResponseForbidden("Access denied.")
    return render(request, "relationship_app/librarian_view.html")

def member_view(request):
    if request.user.profile.role != "member":
        return HttpResponseForbidden("Access denied.")
    return render(request, "relationship_app/member_view.html")
