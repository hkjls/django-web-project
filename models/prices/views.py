#import serialize
from models.assets.crud import crud
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import price
from .serialize import srl_price
from rest_framework.views import APIView
from rest_framework.response import Response

cruding = crud(model=price, srl_model=srl_price, request=None, key=None)

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