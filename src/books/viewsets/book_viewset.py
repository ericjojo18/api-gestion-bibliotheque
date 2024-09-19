from rest_framework import viewsets
from books.models.book_model import BookModel
from books.serializers.book_serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = BookModel.objects.all()
        title = self.request.query_params.get('title',)

        if title is not None:
            queryset = queryset.filter(title=title)
        return queryset