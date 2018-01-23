from django.urls import path

from .views import coaching_home, client_join_coach_view




urlpatterns = [
    path('client_join_coach/', client_join_coach_view, name='client_join_coach_view'),
    path('', coaching_home, name='coaching_home'),
]