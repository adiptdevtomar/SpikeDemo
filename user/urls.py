from django.urls import path, include

from rest_framework.routers import DefaultRouter


from user import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('register/', views.registration_view, name="register"),
    path('login/', views.UserLoginApiView.as_view()),
    path('logout/', views.logoutView, name='logout'),
    path('', include(router.urls))
]
