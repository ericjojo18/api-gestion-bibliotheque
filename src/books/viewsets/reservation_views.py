from django.shortcuts import render
from rest_framework import viewsets
from books.serializers.reservation_serializer import ReservationSerializer
from books.models.reservation_model import ReservationModel


# Create your views here.
class ReservationViewset(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = ReservationModel.objects.all()