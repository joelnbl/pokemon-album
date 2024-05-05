from django.urls import path
from . import views

urlpatterns = [
    path('buy_booster_pack/', views.buy_booster_pack, name='buy_booster_pack'),
    path('pokemon_details/<int:pokemon_id>/', views.pokemon_details, name='pokemon_details'),
    path('view_album/', views.view_album, name='view_album'),
]
