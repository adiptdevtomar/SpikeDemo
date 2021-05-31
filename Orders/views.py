from django.shortcuts import render
from django.http import Http404
from django.core.serializers import serialize
from collections import defaultdict

#from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Orders.models import OrdersModel
from Orders.serializers import OrderSerializer
from Products.serializers import ProductsSerializer
from Products.models import ProductModel
from Cart.models import CartModel
from CartItems.models import CartItemsModel


@api_view(['POST'])
def PlaceOrderView(request):
    if request.method == "POST":
        cart = CartModel.objects.get(cart_id = request.data["cart_id"])
        cartItems = CartItemsModel.objects.filter(cart_id = request.data["cart_id"])
        for item in cartItems:
            order = OrdersModel()
            order.user = cart.user
            order.product = item.product
            order.quantity = item.quantity
            order.save()
        CartItemsModel.objects.filter(cart_id = request.data["cart_id"]).delete()
        cart.subtotal = 0.00
        cart.tax_amount = 0.00
        cart.total = 0.00
        cart.saveUpdate()
        return Response({"message": "Order PLaced Successfully"}, status = 200)


@api_view(['POST'])
def GetRecommendation(request):
    if request.method == "POST":
        orders = OrdersModel.objects.all()
        JsonOrders = list(orders.values())
        allRecommendations = recommend(JsonOrders, request.data["product_id"])
        JsonResponse = []
        for product in allRecommendations:
            JsonResponse.append(ProductModel.objects.get(id = product[1]))
        serializer = ProductsSerializer(JsonResponse, many = True, context={"request":request})
        return Response(serializer.data, status = 200)


def recommend(dataset, product_id):

    usersPerItem = defaultdict(set)
    itemsPerUser = defaultdict(set)

    for d in dataset:
        user,item = d['user_id'], d['product_id']
        usersPerItem[item].add(user)
        itemsPerUser[user].add(item)

    iD = product_id
    similarities = []
    users = usersPerItem[iD]
    for i2 in usersPerItem:
        if i2 == iD: continue
        sim = Jaccard(users, usersPerItem[i2])
        similarities.append((sim,i2))
    similarities.sort(reverse=True)
    return similarities

def Jaccard(s1, s2):
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    return numer / denom
