########## Created routes and build function-based views (FBVs) to handle web pages.
from django.urls import path
from . import views
# from .views import (
#     ItemListView, ItemDetailView,
#     ItemCreateView, ItemUpdateView, ItemDeleteView,
# )

######### URL Routing for CBVs ################
urlpatterns = [
    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('register/', views.register, name='register'),
    path('', ItemListView.as_view(), name='item-list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    # path('item/add/', ItemCreateView.as_view(), name='item-add'),
    # path('item/<int:pk>/edit/', ItemUpdateView.as_view(), name='item-edit'),
    # path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]
