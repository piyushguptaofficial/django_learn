from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('register/', views.register, name='register'),
    path('', ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]
