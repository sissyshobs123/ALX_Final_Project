from django.urls import path
from .views import CategoryListCreateView, ItemCreateView
#from .views import itemlistCreateView --> Comment this because i needed to use ItemCreateView
urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    #path('items/', ItemListCreateView.as_view(), name='item-list'),
    path('items/', ItemCreateView.as_view(), name='item-create'),
]
