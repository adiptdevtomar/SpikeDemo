from django.urls import path
from Cart import views

urlpatterns = [
    path("getCart/<str:nm>", views.getCartView),
]
