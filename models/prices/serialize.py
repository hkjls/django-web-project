from rest_framework import serializers
from models.prices.models import price

class srl_price(serializers.ModelSerializer):
			class Meta:
						model = price
						fields = "__all__"