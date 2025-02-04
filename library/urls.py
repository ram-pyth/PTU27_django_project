from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_nm'),
    path('authors/', views.get_authors, name='authors-all'),
]
