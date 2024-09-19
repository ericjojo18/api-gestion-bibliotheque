from django.shortcuts import render
from books.models.reservation_model import ReservationModel
from rest_framework import serializers



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationModel
        fields = "__all__"