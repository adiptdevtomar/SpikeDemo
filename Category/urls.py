from django.urls import path
from Category import views


urlpatterns = [
    path("category/", views.CategoriesView),
    path("category/<str:nm>", views.CategoryView),
]
