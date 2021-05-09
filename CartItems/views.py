from django.shortcuts import render
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from CartItems.serializers import CartItemSerializer, RemoveCartItemSerializer
from Cart.models import CartModel
from CartItems.models import CartItemsModel
from Products.models import ProductModel
from Products.serializers import ProductsSerializer

from decimal import Decimal


@api_view(["POST"])
def addItemToCartView(request):
    if CartItemsModel.objects.filter(cart = request.data["cart"], product = request.data["product"]).exists():
        return Response({"message":"Item Already Exists"},status = status.HTTP_400_BAD_REQUEST)
    serializer = CartItemSerializer(data = request.data, context={"request":request})
    if serializer.is_valid():
        serializer.save()
        cart = CartModel.objects.get(cart_id = serializer.data["cart"])
        product = ProductModel.objects.get(id = serializer.data["product"])
        cart.subtotal = Decimal(cart.subtotal) + (Decimal(product.price) * Decimal(serializer.data["quantity"]))
        cart.tax_amount = Decimal(cart.subtotal) * Decimal(cart.tax_percentage)
        cart.total = cart.tax_amount + cart.subtotal
        cart.saveUpdate()
        return Response({"message":"Added to Cart Successfully"}, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def RemoveItemFromCart(request):
    serializer = RemoveCartItemSerializer(data = request.data, context={"request":request})
    if serializer.is_valid():
        try:
            cartItem = CartItemsModel.objects.get(cart = serializer.data["cart"], product = serializer.data["product"])
            cart = CartModel.objects.get(cart_id = serializer.data["cart"])
            product = ProductModel.objects.get(id = serializer.data["product"])
            cart.subtotal = Decimal(cart.subtotal) - (Decimal(product.price) * Decimal(cartItem.quantity))
            cart.tax_amount = Decimal(cart.subtotal) * Decimal(cart.tax_percentage)
            cart.total = cart.tax_amount + cart.subtotal
            cart.saveUpdate()
            CartItemsModel.objects.filter(cart = serializer.data["cart"], product = serializer.data["product"]).delete()
            return Response({"message":"Deleted Successfully"},status = status.HTTP_201_CREATED)
        except CartItemsModel.DoesNotExist:
            raise Http404("Cart Item not Found")
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
