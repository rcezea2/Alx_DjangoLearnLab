from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("books/list_books/", views.list_books, name="list_books"),
    path("books/LibraryDetailView/", views.LibraryDetail.as_view(), name="library_detail"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("register", views.register),
    path("login", LoginView.as_view(template_name="relationship_app/login.html", next_page="dashboard"), name="login"),
    path("logout", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("home", views.home, name="dashboard"),
    path("admin_view", views.admin_view, name="admin_view"),
    path("librarian_view", views.librarian_view, name="librarian_view"),
    path("member_view", views.member_view, name="member_view"),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book')

]
