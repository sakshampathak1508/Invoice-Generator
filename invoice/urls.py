from django.urls import path

from .views import ItemApiView, ItemListApiView,BillPdfApiView

urlpatterns = [
  path('all-items/', ItemApiView.as_view(), name='items'),
  path('item-list/', ItemListApiView.as_view(), name='item-list'),
  path('invoice-pdf/', BillPdfApiView.as_view(), name='item-list'),
]
