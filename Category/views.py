from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Category import models, serializers


@api_view(["GET","POST"])
def CategoriesView(request):
    if request.method == "GET":
        category = models.CategoryModel.objects.all()
        serializer = serializers.CategorySerializer(category, many = True, context={"request":request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = serializers.CategorySerializer(data = request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


@api_view(['GET','PUT','DELETE'])
def CategoryView(request,nm):
    try:
        category = models.CategoryModel.objects.get(id = nm)
    except models.CategoryModel.DoesNotExist:
        raise Http404("Not Found")

    if request.method == "GET":
        serializer = serializers.CategorySerializer(product,context={"request":request})
        return Response(serializer.data)

    if request.method == "DELETE":
        category.delete()
        return Response("Deleted Successfully",status = status.HTTP_204_NO_CONTENT)
