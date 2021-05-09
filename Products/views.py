from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from Products import serializers
from Products import models

@api_view(['GET'])
def GetAppProductsOfCategoryView(request, nm):
    if request.method == "GET":
        try:
            category = models.CategoryModel.objects.get(id = nm)
        except models.CategoryModel.DoesNotExist:
            raise Http404("Category Not Found")

        products = models.ProductModel.objects.filter(category=nm)
        serializer = serializers.ProductsSerializer(products, many = True, context={"request":request})
        return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
def GetProductView(request):
    if request.method == "GET":
        products = models.ProductModel.objects.all()
        serializer = serializers.ProductsSerializer(products, many = True, context={"request":request})
        return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
def AddNewProductView(request):
    if request.method == "POST":
        serializer = serializers.ProductSerializer(data = request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def GetSingleProductView(request,nm):
    try:
        product = models.ProductModel.objects.get(id = nm)
    except models.ProductModel.DoesNotExist:
        raise Http404("Not Found")

    if request.method == "GET":
        serializer = serializers.ProductSerializer(product,context={"request":request})
        return Response(serializer.data)


@api_view(['DELETE'])
@csrf_exempt
def DeleteProductView(request,nm):
    try:
        product = models.ProductModel.objects.get(id = nm)
    except models.ProductModel.DoesNotExist:
        raise Http404("Not Found")

    if request.method == "DELETE":
        product.delete()
        return Response("Deleted Successfully",status = status.HTTP_204_NO_CONTENT)


"""
class ImageView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        all_images = models.ImageModel.objects.all()
        serializer = serializers.ImageSerializer(all_images, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        # converts querydict to original dict
        images = dict((request.data).lists())['images']
        flag = 1
        arr = []
        for img_name in images:
            file_serializer = serializers.ImageSerializer(data={"image":img_name})
            if file_serializer.is_valid():
                file_serializer.save()
                arr.append(file_serializer.data)
            else:
                flag = 0

        if flag == 1:
            return Response(arr, status=status.HTTP_201_CREATED)
        else:
            return Response(arr, status=status.HTTP_400_BAD_REQUEST)"""
