from django.urls import path
from .views import (
    CategoryListCreateView, ItemListCreateView, 
    UpdatePriceView, ListItemsView, ItemDetailView, 
)

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("items/", ItemListCreateView.as_view(), name="item-list-create"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),  # 👈 NEW
    path("items/<int:pk>/update-price/", UpdatePriceView.as_view(), name="update-price"),
    path("items/list/", ListItemsView.as_view(), name="list-items"),
]
