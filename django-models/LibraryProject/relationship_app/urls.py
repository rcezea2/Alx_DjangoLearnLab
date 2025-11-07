from django.urls import path
from .views import list_books, LibraryDetail

urlpatterns = [
    path("list_books/", list_books, name="list_books"),
    path("LibraryDetailView/", LibraryDetail.as_view(), name="library_detail")
]
