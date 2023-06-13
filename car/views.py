from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Car, CarSerializer,
    Reservation, ReservationSerializer,
)


# ---------------------------------
# FixView
# ---------------------------------
class FixView(ModelViewSet):
    pass


# ---------------------------------
# CarView
# ---------------------------------
class CarView(FixView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# ---------------------------------
# ReservationView
# ---------------------------------
class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
