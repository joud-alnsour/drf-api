from rest_framework import generics
from .serializers import ApiSerializer
from apis.models import Api


class ApisListAPIView(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class ApisDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer