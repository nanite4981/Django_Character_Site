from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.characters, name='characters'),
    path('characters/details/<int:id>', views.details, name='details'),
]