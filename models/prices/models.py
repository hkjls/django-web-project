from django.db import models

class price(models.Model):
    id = models.IntegerField(primary_key=True)
    p_purchase = models.FloatField(default=0.00)
    p_sale = models.FloatField(default=0.00)
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"price : {self.p_purchase}/{self.p_sale}"