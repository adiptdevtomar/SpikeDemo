from django.urls import path
from Products import views

urlpatterns = [
    path("getProducts/", views.ProductsView),
    path("product/<str:nm>", views.ProductView),
]

"""path("images",views.ImageView.as_view(),name="images")"""
