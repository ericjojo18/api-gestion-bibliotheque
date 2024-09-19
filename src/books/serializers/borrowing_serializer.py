from rest_framework import serializers
from books.models.borrowing_model import BorrowingModel

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowingModel
        fields = '__all__'
        