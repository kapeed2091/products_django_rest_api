from django.conf.urls import url

from products.views import product_match

urlpatterns = [
    url(r'^product_match/$', product_match),
]
