from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('author', 'publication_year')
    list_filter = ('title', 'author', 'publication_year')

admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):

    # Fields visible in Django Admin
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    # Fields to show when creating a new user in the admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo"),
        }),
    )

    list_display = ("username", "email", "date_of_birth", "is_staff")
    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.register(CustomUser, CustomUserAdmin)
