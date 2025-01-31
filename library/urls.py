from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_nm'),
    path('knygos/', views.books, name='books_nm'),
]
