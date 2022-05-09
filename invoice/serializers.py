from rest_framework import serializers
from .models import Item,Order,ItemList


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = '__all__'