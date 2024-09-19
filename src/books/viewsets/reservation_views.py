from django.shortcuts import render
from rest_framework import viewsets
from books.serializers.reservation_serializer import ReservationSerializer
from books.models.reservation_model import ReservationModel


# Create your views here.
class ReservationViewset(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects.all()
    
    @csrf_exempt
    def reservation_detail(request, id):
        try :
            reservation = ReservationModel.objects.get(id=id)
        except ReservationModel.DoesNotExist : 
            return HttpResponse(status=404)
        
        if request.method == 'GET':
            serializer =  ReservationSerializer(reservation)
            return JsonResponse(serializer.data)
    
    
    @csrf_exempt
    def reservation_detail_by_user(request, id):
        try :
            reservation = ReservationModel.objects.filter(user = id)
        except ReservationModel.DoesNotExist : 
            return HttpResponse(status=404)
        
        
        if request.method == 'GET':
            serializer =  ReservationSerializer(reservation,many=True)
            return JsonResponse(serializer.data, safe=False)