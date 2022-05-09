from .models import Item,Order,ItemList
from .serializers import ItemSerializer,ItemListSerializer,OrderSerializer
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .helper import html_to_pdf 
from django.template.loader import render_to_string

class ItemApiView(APIView):
    def get(self, request, format=None):
        it = Item.objects.all()
        serializer = ItemSerializer(it, many=True)
        return Response(serializer.data)

class ItemListApiView(APIView):
    def put(self, request, format=None):
        lid = request.data.get('lid', None)
        obj = ItemList.objects.filter(id=lid).first()
        serializer = ItemListSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def post(self, request, format=None):
        item_list = request.data.get('item_list',[])
        row_obj = []
        oid, created = Order.objects.get_or_create(order_name = request.data.get('name',''))
        for idx in item_list:
            idx['order'] = oid.id
            serializer_row_data = ItemListSerializer(data=idx)
            if serializer_row_data.is_valid():
                row_obj.append(serializer_row_data)
        for item in row_obj:
            item.save()
        return Response("Success", status=200)

class BillPdfApiView(APIView):
    def get(self, request, *args, **kwargs):
        oid = request.GET.get('oid', None)
        data = ItemList.objects.filter(order=oid)
        pdf = html_to_pdf('invoice/invoice.html',{"data":data})
        return HttpResponse(pdf, content_type='application/pdf')
