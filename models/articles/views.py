#import serialize
from models.assets.crud import crud
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import article
from .serialize import srl_article
from rest_framework.views import APIView
from rest_framework.response import Response

cruding = crud(model= article, srl_model= srl_article, request= None, key = None)

@permission_classes([IsAuthenticated])
class read(APIView):
    def get(self, request):
        cruding.r = request
        return cruding.read()

@permission_classes([IsAuthenticated])
class create(APIView):
    def post(self, request):
        cruding.r = request
        return cruding.create()

@permission_classes([IsAuthenticated])
class update(APIView):
    def post(self, request, pk):
        cruding.r = request
        cruding.k = pk
        return cruding.update()
    
@permission_classes([IsAuthenticated])
class delete(APIView):
    def post(self, request, pk):
        cruding.r = request
        cruding.k = pk
        return cruding.delete()
