from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from books.serializers.reservation_serializer import ReservationSerializer
from books.models.reservation_model import ReservationModel


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
    
    
    @action(detail=False, methods=['get'])
    def reservation_detail_by_user(self, request, user_id=None):
        try:
            reservations = ReservationModel.objects.filter(user=user_id)
        except ReservationModel.DoesNotExist:
            return HttpResponse(status=404)
        
        serializer = ReservationSerializer(reservations, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    
    @action(detail=False, methods=['get'])
    def reservation_detail_by_book(self, request, book_id=None):
        reservations = ReservationModel.objects.filter(book=book_id)
        if not reservations.exists():
            return HttpResponse(status=404)
        
        serializer = ReservationSerializer(reservations, many=True)
        return JsonResponse(serializer.data, safe=False)

        
