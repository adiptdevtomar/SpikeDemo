from rest_framework import viewsets, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import  GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status

from user import permissions
from user import serializers
from user import models
from Cart.models import CartModel


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = serializers.RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.create(request.data)
            data['response'] = "Successfully registered a new user"
        else:
            data = serializer.errors
        return Response(data)


class UserProfileViewSet(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet
                         ):

    """Serializer for User Profile Model"""
    serializer_class = serializers.RegistrationSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.UpdateOwnProfile, IsAuthenticated]



@api_view(['POST',])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logoutView(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({"response":"Logout Successful"},status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        cart = CartModel.objects.get(user_id = user.id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'cart_id': cart.cart_id
        })
