from django.urls import path
from Brands import views


urlpatterns = [
    path("brands/", views.BrandsView),
    path("brand/<str:nm>", views.BrandView),
]
