from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from books.serializers.borrowing_serializer import BorrowingSerializer
from books.models.borrowing_model import BorrowingModel
from books.models.book_model import BookModel
from users.models import UserModel


class BorrowingViewSet(viewsets.ModelViewSet):
    serializer_class = BorrowingSerializer
    queryset = BorrowingModel.objects.all()
    
    @action(detail=True, methods=['get'])
    def borrowing_detail(self, request, pk=None):
        try:
            reservation = BorrowingModel.objects.get(id=pk)
        except BorrowingModel.DoesNotExist:
            return HttpResponse(status=404)
        
        serializer = BorrowingSerializer(reservation)
        return JsonResponse(serializer.data)
    
    
    @action(detail=False, methods=['get'])
    
    def borrowing_detail_by_user(self, request, user_id=None):
        try:
            reservations = BorrowingModel.objects.filter(user=user_id)
        except BorrowingModel.DoesNotExist:
            return HttpResponse(status=404)
        
        serializer = BorrowingSerializer(reservations, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    
    @action(detail=False, methods=['get'])
    def borrowing_detail_by_book(self, request, book_id=None):
        reservations = BorrowingModel.objects.filter(book=book_id)
        if not reservations.exists():
            return HttpResponse(status=404)
        
        serializer = BorrowingSerializer(reservations, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        user_id = data.get('user')
        
        try:
            user = UserModel.objects.get(id=user_id)
        except UserModel.DoesNotExist:
            return Response({'error': 'Utilisateur introuvable'}, status=status.HTTP_404_NOT_FOUND)

        book_id = data.get('book')  
        try:
            book = BookModel.objects.get(id=book_id)
        except BookModel.DoesNotExist:
            return Response({'error': 'Livre introuvable'}, status=status.HTTP_404_NOT_FOUND)
        
        
        if book.quantity <= 0:
            return Response({'error': 'Aucun exemplaire disponible'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        serializer = BorrowingSerializer(data=data)
        if serializer.is_valid():
            
            book.quantity -= 1
            book.save()
            
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)