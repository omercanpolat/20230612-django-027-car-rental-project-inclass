from rest_framework import serializers

from .models import (
    Car,
    Reservation
)


# ---------------------------------
# FixSerializer
# ---------------------------------
class FixSerializer(serializers.ModelSerializer):
    pass


# ---------------------------------
# CarSerializer
# ---------------------------------
class CarSerializer(FixSerializer):

    class Meta:
        model = Car
        exclude = []


# ---------------------------------
# ReservationSerializer
# ---------------------------------
class ReservationSerializer(FixSerializer):

    class Meta:
        model = Reservation
        exclude = []