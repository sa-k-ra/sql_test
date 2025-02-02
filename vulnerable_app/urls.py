from django.urls import path
from . import views

app_name = 'vulnerable_app'
urlpatterns = [
    path('search/', views.search_user, name='search_user'),
]

