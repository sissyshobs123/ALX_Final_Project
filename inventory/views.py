from rest_framework import generics, permissions
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#class ItemListCreateView(generics.ListCreateAPIView):
 #   queryset = Item.objects.all()
  #  serializer_class = ItemSerializer

# Create Item (POST /items/)
class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]