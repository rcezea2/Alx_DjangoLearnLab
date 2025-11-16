from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can edit book"),
            ("can_delete_book", "Can delete book")
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices={
        "admin": "Admin",
        "librarian": "Librarian",
        "member": "Member"
    }, default="member")

    def __str__(self):
        return f"{self.user.username} is a {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


class User(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
