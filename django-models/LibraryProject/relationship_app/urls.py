from django.urls import path
from .views import list_books, LibraryDetail, RegisterView, Login, Logout, home

urlpatterns = [
    path("books/list_books/", list_books, name="list_books"),
    path("books/LibraryDetailView/", LibraryDetail.as_view(), name="library_detail"),
    path("register", RegisterView.as_view(), name="register"),
    path("login", Login.as_view(), name="login"),
    path("logout", Logout.as_view(), name="logout"),
    path("home", home, name="dashboard")

]
