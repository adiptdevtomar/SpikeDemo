from django.urls import path

from Orders import views

urlpatterns = [
    path("placeOrder/", views.PlaceOrderView),
    path("getRecommendation/", views.GetRecommendation)
]

"""path("placeOrder/", views.PlaceOrderView.as_view({'post': 'create'})),"""
