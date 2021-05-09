from django.urls import path
from Products import views

urlpatterns = [
    path("addNewProduct/", views.AddNewProductView),
    path("getProducts/", views.GetProductView),
    path("getProductDetails/<str:nm>", views.GetSingleProductView),
    path("deleteProduct/<str:nm>", views.DeleteProductView),
    path("getAllProductsOfCategory/<str:nm>", views.GetAppProductsOfCategoryView),
]

"""path("images",views.ImageView.as_view(),name="images")"""
