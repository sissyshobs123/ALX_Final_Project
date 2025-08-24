from django.urls import path
from .views import (
    CategoryListCreateView, ItemListCreateView, 
    UpdatePriceView, ListItemsView, ItemDetailView, 
)

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("items/", ItemListCreateView.as_view(), name="item-list"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("items/<int:pk>/update-price/", UpdatePriceView.as_view(), name="update-price"),
    path("items/list/", ListItemsView.as_view(), name="item-list-filter"),
]

