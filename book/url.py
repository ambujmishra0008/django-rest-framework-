
from .views import booklist
from django.urls import path

urlpatterns = [
    path('booklist', booklist)
]

