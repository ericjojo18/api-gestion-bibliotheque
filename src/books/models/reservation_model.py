from django.db import models
from users.models import UserModel
from .book_model import  BookModel


class ReservationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)  # pour  un utilisateur qui a reserve un livre
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, null=True)  # pour  un livre réserve
    reservation_at = models.DateField(auto_now_add=True) # Date de reservation
    status = models.BooleanField(default=True) # Status de la reservation


