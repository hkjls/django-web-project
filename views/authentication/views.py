from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class pair_serializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token
    
class pair_view(TokenObtainPairView):
    serializer_class = pair_serializer
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def token_access(request):
    path_routes = [
        '/api/token/',
        '/api/token/refresh'
    ]
    return Response(path_routes)