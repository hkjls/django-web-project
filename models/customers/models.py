from django.db import models
from models.articles.models import article

class customer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    tel = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    type = models.CharField(max_length=15)

    class Meta:
        verbose_name="customer"
        ordering = ['id']

    def __str__(self):
        return self.name

class order_customer(models.Model):
    id = models.IntegerField(primary_key=True)
    Ref = models.CharField(max_length=125)
    status = models.IntegerField(default=0)
    date = models.DateField()
    id_customer = models.ForeignKey(customer, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.Ref
    
class order_list_customer(models.Model):
    id = models.IntegerField(primary_key=True)
    qty = models.FloatField(default=0.0)
    price = models.FloatField(default=0.00)
    id_article = models.ForeignKey(article, on_delete=models.CASCADE, default='')
    id_order = models.ForeignKey(order_customer, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.id_article} - {self.qty}"

class delivery_customer(models.Model):
    id = models.IntegerField(primary_key=True)
    Ref = models.CharField(max_length=125)
    status = models.IntegerField(default=0)
    date = models.DateField()
    id_order = models.ForeignKey(order_customer, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"order {self.Ref}"

class invoice_customer(models.Model):
    id = models.IntegerField(primary_key=True)
    Ref = models.CharField(max_length=125)
    status = models.IntegerField(default=0)
    id_delivery_customer = models.OneToOneField(delivery_customer, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"invoice {self.Ref}"

class payment_customer(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=125)
    code = models.CharField(max_length=125)
    status = models.IntegerField(default=0)
    id_invoice_customer = models.ForeignKey(invoice_customer, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"payment {self.code}"