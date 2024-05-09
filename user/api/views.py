
from django.contrib.auth.models import User
# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

from datetime import timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from common.rest_framework.mixins import APIViewResponseMixin


@api_view(['GET'])
def provide_token(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return Response({'error': 'User is not authenticated'}, status=401)

    # Generate a new token with a one-year expiration
    refresh = RefreshToken.for_user(request.user)
    refresh.set_exp(lifetime=timedelta(days=365))
    token = str(refresh.access_token)
    data = {"token": token}
    return APIViewResponseMixin.success_response(
        message="Token", data=data)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes([AllowAny])
def test(request):
    message = "Success message"
    data = {"key": "value"}
    response = APIViewResponseMixin.success_response(
        message=message, data=data)
    return response
