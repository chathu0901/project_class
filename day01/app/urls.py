from django.urls import path
from . import views

urlpatterns = [
    path('Category/',views.category_view),
    path('Unit/',views.unit_view),
    path('test/', views.test),
    path('Item/', views.item_view),
    path('supplier/', views.supplier_view),
    path('order/', views.order_view),
    path('employee/', views.employee_view),
]
