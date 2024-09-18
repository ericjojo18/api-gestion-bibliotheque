from django.db import models
from books.models.book_model  import BookModel
from  users.models import UserModel


class BorrowingModel(BookModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='borrowings') # pour selection un utilisateur
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='borrowings') # pour selection un livre
    borrowed_at = models.DateTimeField(auto_now_add=True) # la date du livre a été emprunté
    return_at = models.DateTimeField(null=True, blank=True) # la date prevue du reto
    returned = models.BooleanField(default=False) # Pour indiquer si le livre a été retourne

