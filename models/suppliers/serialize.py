from rest_framework import serializers
from models.suppliers.models import supplier, order_list_supplier, order_supplier, delivery_supplier, invoice_supplier, payment_supplier

class srl_supplier(serializers.ModelSerializer):
			class Meta:
						model = supplier
						fields = "__all__"

class srl_order_list_supplier(serializers.ModelSerializer):
			class Meta:
						model = order_list_supplier
						fields = "__all__"

class srl_order_supplier(serializers.ModelSerializer):
			class Meta:
						model = order_supplier
						fields = "__all__"
					
class srl_delivery_supplier(serializers.ModelSerializer):
			class Meta:
						model = delivery_supplier
						fields = "__all__"
						
class srl_invoice_supplier(serializers.ModelSerializer):
			class Meta:
						model = invoice_supplier
						fields = "__all__"

class srl_payment_supplier(serializers.ModelSerializer):
			class Meta:
						model = payment_supplier
						fields = "__all__"