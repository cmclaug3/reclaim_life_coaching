from django.urls import path, include

from member.views import become_coach

urlpatterns = [
    path('become_coach/', become_coach, name='become_coach'),
]