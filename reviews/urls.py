from django.urls import path
from .views import ReviewCreate

urlpatterns = [
    path('create/', ReviewCreate.as_view())
]
