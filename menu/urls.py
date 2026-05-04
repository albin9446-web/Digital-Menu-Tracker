from django.urls import path
from .views import MenuListView, OrderCreateView

urlpatterns = [
    path('menu/', MenuListView.as_view()),
    path('order/', OrderCreateView.as_view()),
]