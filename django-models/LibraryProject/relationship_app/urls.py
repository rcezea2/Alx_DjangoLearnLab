from django.urls import path
from .views import list_books, LibraryDetail, RegisterView, Login, Logout, home
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("books/list_books/", list_books, name="list_books"),
    path("books/LibraryDetailView/", LibraryDetail.as_view(), name="library_detail"),
    path("register", RegisterView.as_view(), name="register"),
    path("login", LoginView.as_view(template_name="relationship_app/login.html", next_page="dashboard"), name="login"),
    path("logout", Logout.as_view(template_name = "relationship_app/logout.html"), name="logout"),
    path("home", home, name="dashboard")

]
