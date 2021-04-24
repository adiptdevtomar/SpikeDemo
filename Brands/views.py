from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from Brands import models, serializers


@api_view(["GET","POST"])
def BrandsView(request):
    if request.method == "GET":
        brands = models.BrandModel.objects.all()
        serializer = serializers.BrandSerializer(brands, many = True, context={"request":request})
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = serializers.BrandSerializer(data = request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


@api_view(['GET','PUT','DELETE'])
def BrandView(request,nm):
    try:
        brand = models.BrandModel.objects.get(id = nm)
    except models.BrandModel.DoesNotExist:
        raise Http404("Not Found")

    if request.method == "GET":
        serializer = serializers.BrandSerializer(product,context={"request":request})
        return Response(serializer.data)

    if request.method == "DELETE":
        brand.delete()
        return Response("Deleted Successfully",status = status.HTTP_204_NO_CONTENT)
