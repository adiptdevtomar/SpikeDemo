from django.shortcuts import render
from django.http import Http404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Cart.models import CartModel
from Cart.serializers import CartSerializer
from CartItems.models import CartItemsModel
from CartItems.serializers import CartItemSerializer
from Products.models import ProductModel
from Products.serializers import ProductsSerializer


def getProductFromId(request, id, quantity):
    product = ProductModel.objects.filter(id = id)
    serializer = ProductsSerializer(product, many = True, context={"request":request})
    return {"id":serializer.data[0]["id"],
            "name":serializer.data[0]["name"],
            "price":serializer.data[0]["price"],
            "image":serializer.data[0]["image"],
            "quantity": quantity}


def getCartItems(request, id):
    items = CartItemsModel.objects.filter(cart_id = id)
    serializer = CartItemSerializer(items, many = True, context={"request":request})
    returnList = []
    for i in range(len(items)):
        returnList.append(getProductFromId(request, items[i], items[i].quantity))
    return returnList


@api_view(['GET'])
def getCartView(request, nm):
    try:
        cart = CartModel.objects.get(cart_id = nm)
    except CartModel.DoesNotExist:
        raise Http404("Category Not Found")


    items = getCartItems(request, nm)
    cart = CartModel.objects.filter(cart_id = nm)
    serializer = CartSerializer(cart, many = True, context={"request":request})
    return Response({"user":serializer.data[0]["user"],
                    "cart_id":serializer.data[0]["cart_id"],
                    "tax_amount":serializer.data[0]["tax_amount"],
                    "subtotal":serializer.data[0]["subtotal"],
                    "total":serializer.data[0]["total"],
                    "tax_percentage":serializer.data[0]["tax_percentage"],
                    "cart_items":items,
                    }, status = status.HTTP_200_OK)
