

from django.urls import path
from . import views


urlpatterns = [
    path('payment_success/',views.payment_success,name='payment_success'),
    path('shipping_address/',views.shipping_address,name='shipping_address'),
    path('checkout/',views.checkout,name='checkout'),
    path('billing_info/',views.billing_info,name='billing_info'),
    path('process_order/',views.process_order,name='process_order'),
    path('shipped_status/',views.shipped_status,name='shipped_status'),
    path('orders/<int:pk>', views.orders,name='orders')



   
]
