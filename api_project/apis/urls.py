from django.urls import path
from apis.api.viewset import (
                                ApisListAPIView,
                                ApisDetailAPIView
                                )

urlpatterns = [
    path('api/v1/api-list', ApisListAPIView.as_view(), name='apis_list'),
    path('api/v1/<int:pk>', ApisDetailAPIView.as_view(), name='api_detail'),

]
