from django.urls import path
from .articles.views import create as create_article, read as read_article, update as update_article, delete as delete_article
from .prices.views import create as create_prices, read as read_prices, update as update_prices, delete as delete_prices
from .customers.views import read as read_customers, create as create_customers
from .customers.views import update as update_customers, delete as delete_customers

from .suppliers.views import read as read_suppliers, create as create_suppliers
from .suppliers.views import update as update_suppliers, delete as delete_suppliers


urlpatterns = [
    path('article/create/', create_article.as_view(), name="create_article"),
    path('article/', read_article.as_view(), name="read_article"),
    path('article/update/<int:pk>', update_article.as_view(), name = "update_article"),
    path('article/delete/<int:pk>', delete_article.as_view(), name="delete_article"),

    path('prices/create/', create_prices.as_view(), name="create_prices"),
    path('prices/', read_prices.as_view(), name="read_prices"),
    path('prices/update/<int:pk>', update_prices.as_view(), name="update_prices"),
    path('prices/delete/<int:pk>', delete_prices.as_view(), name="delete_article"),

    path('customers/<str:customers>', read_customers.as_view(), name="read_customers"),
    path('customers/create_customers/<str:customers>', create_customers.as_view(), name="create_customers"),
    path('customers/update_customers/<str:customers>/<int:pk>', update_customers.as_view(), name="update_customers"),
    path('customers/delete_customers/<str:customers>/<int:pk>', delete_customers.as_view(), name="delete_customers"),

    path('suppliers/<str:suppliers>', read_suppliers.as_view(), name="read_suppliers"),
    path('suppliers/create_suppliers/<str:suppliers>', create_suppliers.as_view(), name="create_suppliers"),
    path('suppliers/update_suppliers/<str:suppliers>/<int:pk>', update_suppliers.as_view(), name="update_suppliers"),
    path('suppliers/delete_suppliers/<str:suppliers>/<int:pk>', delete_suppliers.as_view(), name="delete_suppliers"),
]