from rest_framework import generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Category, Item
from .serializers import CategorySerializer, ItemSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class UpdatePriceView(APIView):
    permission_classes = [IsAuthenticated]

    # PATCH - Partial Update
    def patch(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(
                {"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )

        new_price = request.data.get("price")
        if not new_price:
            return Response(
                {"error": "Price is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        item.price = new_price
        item.save()

        return Response(
            {
                "message": "Price updated successfully (PATCH)",
                "id": item.id,
                "price": item.price,
            }
        )

    # PUT - Full Update (only price in this case)
    def put(self, request, pk):
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(
                {"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )

        new_price = request.data.get("price")
        if not new_price:
            return Response(
                {"error": "Price is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Since it's PUT, we treat it as full replacement of price
        item.price = new_price
        item.save()

        return Response(
            {
                "message": "Price updated successfully (PUT)",
                "id": item.id,
                "price": item.price,
            }
        )


class ListItemsView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # filter by exact fields
    filterset_fields = ["category"]

    # search across fields (partial match)
    search_fields = ["name"]
    ordering_fields = ["name", "price", "created_at"]  # allowed ordering fields
    ordering = ["name"]  # default ordering


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
