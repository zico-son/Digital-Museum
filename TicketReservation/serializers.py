from rest_framework import serializers
from .models import *
from django.db import transaction



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'ticket_type','price']



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','ticket','amount']

    
    
class ViewOrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    ticket = TicketSerializer()
    class Meta:
        model = OrderItem
        fields = ['id','ticket','amount','total_price']
    def get_total_price(self,orderitem:OrderItem):
        return orderitem.ticket.price * orderitem.amount
    
class ViewOrderSerializer(serializers.ModelSerializer):
    tickets = ViewOrderItemSerializer(many=1)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ['id','first_name','last_name','email','phone','tickets','date','created_at','total_price']
    
    def get_total_price(self,order:Order):
        return sum([item.amount * item.ticket.price for item in order.tickets.all()])
    
 
class OrderItemTestSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = OrderItem
        fields = ['id','ticket','amount','total_price']
    def get_total_price(self,orderitem:OrderItem):
        return orderitem.ticket.price * orderitem.amount

    
class OrderSerializer(serializers.ModelSerializer):
    tickets = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id','first_name','last_name','email','phone','date','tickets']
    def create(self, validated_data):
        with transaction.atomic():
           tickets = validated_data.pop('tickets')
           order = Order.objects.create(**validated_data)
           ticket_items = [
               OrderItem(  
                    order=order,
                    ticket=item['ticket'],
                    amount=item['amount'],
               )for item in tickets
           ]
           order_item =OrderItem.objects.bulk_create(ticket_items)
           return order
           

        


 


    
    
    

    