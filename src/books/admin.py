from django.contrib import admin
from books.models.book_model import BookModel
from books.models.borrowing_model import BorrowingModel
from books.models.reservation_model import ReservationModel
# Register your models here.

admin.site.register(BookModel)
admin.site.register(BorrowingModel)
admin.site.register(ReservationModel)