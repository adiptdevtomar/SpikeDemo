from django.urls import path
from CartItems import views

urlpatterns = [
    path("addItemToCart/", views.addItemToCartView),
    path("removeItemFromCart/", views.RemoveItemFromCart),
]
