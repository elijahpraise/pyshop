from django.urls import path
from .views import index, detail

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', detail, name='detail')
]