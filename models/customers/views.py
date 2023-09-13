#import serialize
from models.assets.crud import crud
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from .models import customer, order_customer, order_list_customer, delivery_customer, invoice_customer, payment_customer
from .serialize import srl_customer, srl_order_customer, srl_order_list_customer, srl_delivery_customer, srl_invoice_customer, srl_payment_customer
from rest_framework.views import APIView
from rest_framework.response import Response

models_name = ['customers', 
               'order_customers', 
               'order_list_customers', 
               'delivery_customers', 
               'invoice_customers', 
               'payment_customers',]

models_list = [customer,
               order_customer,
               order_list_customer,
               delivery_customer,
               invoice_customer,
               payment_customer,]

serial_list = [srl_customer,
               srl_order_customer,
               srl_order_list_customer,
               srl_delivery_customer,
               srl_invoice_customer,
               srl_payment_customer,]

def get_request(crud, models_name, model_request, model_list, serial_list, request, key = None):
    
    for m in range(len(models_name)):
        if models_name[m] == model_request:
            cruding = crud(request, model_list[m], serial_list[m], key)
            return cruding
    return False

@permission_classes([IsAuthenticated])
class read(APIView):
    def get(self, request, customers):
        result = get_request(crud, models_name, customers, models_list, serial_list, request)
        if result:
            return result.read()
        else:
            return Response(404)
        
@permission_classes([IsAuthenticated])
class create(APIView):
    def post(self, request, customers):
        result = get_request(crud, models_name, customers, models_list, serial_list, request)
        if result:
            return result.create()
        else:
            return Response(404)

@permission_classes([IsAuthenticated])
class update(APIView):
    def post(self, request, customers, pk):
        result = get_request(crud, models_name, customers, models_list, serial_list, request, pk)
        if result:
            return result.update()
        else:
            return Response(404)

@permission_classes([IsAuthenticated])
class delete(APIView):
    def post(self, request, customers, pk):
        result = get_request(crud, models_name, customers, models_list, serial_list, request, pk)
        if result:
            return result.delete()
        else:
            return Response(404)