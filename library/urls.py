from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='h'),
    path('book1', book1_view, name='b1'),
    path('book2', book2_view, name='b2'),
    path('book3', book3_view, name='b3'),
    path('book4', book4_view, name='b4'),
    path('book5', book5_view, name='b5'),
]