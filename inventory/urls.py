from django.urls import path
from .views import CategoryListCreateView, ItemListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('items/', ItemListCreateView.as_view(), name='item-list'),
]
