from django.urls import path
from apis.api.viewset import (
                                ThingsListAPIView,
                                ThingsDetailAPIView
                                )

urlpatterns = [
    path('api/v1/things-list', ThingsListAPIView.as_view(), name='apis_list'),
    path('api/v1/<int:pk>', ThingsDetailAPIView.as_view(), name='api_detail'),

]