from django.db import models
from users.models import UserModel
from .book_model import  BookModel


class ReservationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)  
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, null=True)  
    reservation_at = models.DateField(auto_now_add=True) 
    status = models.BooleanField(default=True) 


