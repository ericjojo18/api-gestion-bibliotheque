from books.serializers.borrowing_serializer import BorrowingSerializer
from rest_framework import viewsets
from books.models.borrowing_model import BorrowingModel

class BorrowingViewSet(viewsets.ModelViewSet):
    queryset = BorrowingModel.objects.all()
    serializer_class = BorrowingSerializer