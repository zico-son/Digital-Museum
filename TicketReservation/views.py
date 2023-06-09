from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# Create your views here.



class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class OrderItemViewSet(ModelViewSet):
    queryset = OrderItem.objects.select_related('ticket').all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ViewOrderItemSerializer
        return OrderItemSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.prefetch_related('tickets__ticket').all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ViewOrderSerializer
        return OrderSerializer