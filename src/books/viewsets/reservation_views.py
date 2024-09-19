from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from books.serializers.reservation_serializer import ReservationSerializer
from books.models.reservation_model import ReservationModel
from books.models.book_model import BookModel
from users.models import UserModel
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


class ReservationViewset(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects.all()
    
    @action(detail=True, methods=['get'])
    def reservation_detail(self, request, pk=None):
        try:
            reservation = ReservationModel.objects.get(id=pk)
        except ReservationModel.DoesNotExist:
            return HttpResponse(status=404)
        
        serializer = ReservationSerializer(reservation)
        return JsonResponse(serializer.data)
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
        
        
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            
            book.quantity -= 1
            book.save()
            
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    #@action(detail=True, methods=['get'])
@csrf_exempt
def reservation_detail_by_user(request, id=None):
        user = get_object_or_404(UserModel, id=id)
        reservation = ReservationModel.objects.filter(user_id=user.id)

        if not reservation.exists():
            return HttpResponse(status=204)  

        if request.method == 'GET':
            serializer = ReservationSerializer(reservation, many=True)
            return JsonResponse(serializer.data, safe=False)  
    
    
# def reservation_detail_by_book(self, request, book_id=None):
#         reservations = ReservationModel.objects.filter(book=book_id)
#         if not reservations.exists():
#             return HttpResponse(status=404)
        
#         serializer = ReservationSerializer(reservations, many=True)
#         return JsonResponse(serializer.data, safe=False)
@csrf_exempt
def reservation_detail_by_book(request, id=None):
        book = get_object_or_404(BookModel, id=id)
        reservation = ReservationModel.objects.filter(book_id=book.id)

        if not reservation.exists():
            return HttpResponse(status=204)  

        if request.method == 'GET':
            serializer = ReservationSerializer(reservation, many=True)
            return JsonResponse(serializer.data, safe=False)  
    
    
