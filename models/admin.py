from django.contrib import admin
from .articles.models import article
from .prices.models import price
from .customers.models import customer, order_list_customer, order_customer, delivery_customer, invoice_customer, payment_customer
from .suppliers.models import supplier, order_list_supplier, order_supplier, delivery_supplier, invoice_supplier, payment_supplier

# Register your models here.
admin.site.register(article)
admin.site.register(price)

admin.site.register(customer)
admin.site.register(order_list_customer)
admin.site.register(order_customer)
admin.site.register(delivery_customer)
admin.site.register(invoice_customer)
admin.site.register(payment_customer)

admin.site.register(supplier)
admin.site.register(order_list_supplier)
admin.site.register(order_supplier)
admin.site.register(delivery_supplier)
admin.site.register(invoice_supplier)
admin.site.register(payment_supplier)