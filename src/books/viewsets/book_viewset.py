from rest_framework import viewsets, filters
from books.models.book_model import BookModel
from books.serializers.book_serializer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']