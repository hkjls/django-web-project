from rest_framework import serializers
from models.customers.models import customer, order_list_customer, order_customer, delivery_customer, invoice_customer, payment_customer

class srl_customer(serializers.ModelSerializer):
			class Meta:
						model = customer
						fields = "__all__"

class srl_order_list_customer(serializers.ModelSerializer):
			class Meta:
						model = order_list_customer
						fields = "__all__"

class srl_order_customer(serializers.ModelSerializer):
			class Meta:
						model = order_customer
						fields = "__all__"
					
class srl_delivery_customer(serializers.ModelSerializer):
			class Meta:
						model = delivery_customer
						fields = "__all__"
						
class srl_invoice_customer(serializers.ModelSerializer):
			class Meta:
						model = invoice_customer
						fields = "__all__"

class srl_payment_customer(serializers.ModelSerializer):
			class Meta:
						model = payment_customer
						fields = "__all__"