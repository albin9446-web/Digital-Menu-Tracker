from rest_framework import generics
from .models import Category, MenuItem, Order
from .serializers import CategorySerializer, MenuItemSerializer, OrderSerializer


# 📋 GET → Show all available menu items
class MenuListView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(available=True)
    serializer_class = MenuItemSerializer


# 🛒 POST → Create a new order
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer