from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from users.serializers import UserSerializer


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])  # Allows unauthenticated access
def register_user(request):
    user = UserSerializer(data=request.data)

    if user.is_valid():
        user.save()
        return Response(user.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
