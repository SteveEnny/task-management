
"""
Views for the user API.
"""
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from rest_framework import status

from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.authtoken.models import Token


class Register(generics.CreateAPIView):
    """Create a new user in the sytem"""
    serializer_class = UserSerializer


# class Login(APIView):
#     def post(self, request, **args):
#         """Token generated om login"""
#         serializer = AuthTokenSerializer(request.user, data=request.data)
#         if serializer.is_valid():
#             token = Token.objects.create(user=request.user)
#             return Response({
#                 'token': token.key,
#             })
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):
    """Create a new auth token from user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
