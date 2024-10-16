from rest_framework import serializers
from django.utils import timezone
from .models import Customer, Product, Order, OrderItem

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['uid', 'name', 'contact_number', 'email']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['uid', 'name', 'weight']

    def validate_weight(self, value):
        if value <= 0 or value > 25:
            raise serializers.ValidationError("Weight must be a positive value and less than or equal to 25kg.")
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['uid', 'order_number', 'customer', 'order_date', 'address', 'order_items']

    def validate_order_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Order date cannot be in the past.")
        return value

    def validate(self, data):
        total_weight = sum(item['product'].weight * item['quantity'] for item in data['orderitem_set'])
        if total_weight > 150:
            raise serializers.ValidationError("The total weight of the order cannot exceed 150kg.")
        return data

    def create(self, validated_data):
        order_items_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('orderitem_set')
        instance.customer = validated_data.get('customer', instance.customer)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        OrderItem.objects.filter(order=instance).delete()
        for item_data in order_items_data:
            OrderItem.objects.create(order=instance, **item_data)

        return instance
