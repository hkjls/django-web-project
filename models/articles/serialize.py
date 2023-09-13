from rest_framework import serializers
from models.articles.models import article

class srl_article(serializers.ModelSerializer):
			class Meta:
						model = article
						fields = "__all__"