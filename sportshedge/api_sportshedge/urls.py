# your_app/urls.py
from django.urls import path
from .views import get_current_price_api, get_total_points_api, get_key_api_endpoint

urlpatterns = [
    path('current-price/<str:player_id>/', get_current_price_api, name='get-current-price-api'),
    path('total-points/<str:player_id>/', get_total_points_api, name='get-total-points-api'),
    path('key-api/<str:cricsheet_key>/', get_key_api_endpoint, name='get-key-api'),
]
