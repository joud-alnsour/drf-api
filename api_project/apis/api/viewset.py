from rest_framework import generics
from .serializers import ThingSerializer
from apis.models import api


class ThingsListAPIView(generics.ListCreateAPIView):
    queryset = api.objects.all()
    serializer_class = ThingSerializer


class ThingsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = api.objects.all()
    serializer_class = ThingSerializer