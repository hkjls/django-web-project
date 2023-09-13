#import serialize
from models.assets.crud import crud
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import supplier, order_supplier, order_list_supplier, delivery_supplier, invoice_supplier, payment_supplier
from .serialize import srl_supplier, srl_order_supplier, srl_order_list_supplier, srl_delivery_supplier, srl_invoice_supplier, srl_payment_supplier
from rest_framework.views import APIView
from rest_framework.response import Response

models_name = ['suppliers', 
               'order_suppliers', 
               'order_list_suppliers', 
               'delivery_suppliers', 
               'invoice_suppliers', 
               'payment_suppliers',]

models_list = [supplier,
               order_supplier,
               order_list_supplier,
               delivery_supplier,
               invoice_supplier,
               payment_supplier,]

serial_list = [srl_supplier,
               srl_order_supplier,
               srl_order_list_supplier,
               srl_delivery_supplier,
               srl_invoice_supplier,
               srl_payment_supplier,]

def get_request(crud, models_name, model_request, model_list, serial_list, request, key = None):
    
    for m in range(len(models_name)):
        if models_name[m] == model_request:
            cruding = crud(request, model_list[m], serial_list[m], key)
            return cruding
    return False

@permission_classes([IsAuthenticated])
class read(APIView):
    def get(self, request, suppliers):
        result = get_request(crud, models_name, suppliers, models_list, serial_list, request)
        if result:
            return result.read()
        else:
            return Response(404)
        
@permission_classes([IsAuthenticated])
class create(APIView):
    def post(self, request, suppliers):
        result = get_request(crud, models_name, suppliers, models_list, serial_list, request)
        if result:
            return result.create()
        else:
            return Response(404)
        
@permission_classes([IsAuthenticated])
class update(APIView):
    def post(self, request, suppliers, pk):
        result = get_request(crud, models_name, suppliers, models_list, serial_list, request, pk)
        if result:
            return result.update()
        else:
            return Response(404)

@permission_classes([IsAuthenticated])
class delete(APIView):
    def post(self, request, suppliers, pk):
        result = get_request(crud, models_name, suppliers, models_list, serial_list, request, pk)
        if result:
            return result.delete()
        else:
            return Response(404)