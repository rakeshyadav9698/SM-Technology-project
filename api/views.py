from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from .models import CustomUser, Order
from rest_framework.decorators import action
from .serializers import RegisterSerializer, OrderSerializer, Order, CustomUser
from .permissions import IsAdmin, IsDeliveryMan, IsUser
import stripe
from django.conf import settings
import os
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user.role)
        if user.role == 'admin':
            return Order.objects.all()
        elif user.role == 'delivery':
            return Order.objects.filter(delivery_man=user)
        else:
            return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        user = request.user

        if user.role == 'delivery' and order.delivery_man == user:
            order.status = request.data.get('status', order.status)
            order.save()
            return Response(OrderSerializer(order).data)

        return Response({"success": False, "message": "Unauthorized access."}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['patch'], permission_classes=[IsAdmin])
    def assign(self, request, pk=None):
        try:
            order = self.get_object()
            delivery_man_id = request.data.get('delivery_man_id')

            if not delivery_man_id:
                return Response({
                    "success": False,
                    "message": "Validation error occurred.",
                    "errorDetails": {
                        "field": "delivery_man_id",
                        "message": "This field is required."
                    }
                }, status=status.HTTP_400_BAD_REQUEST)

            delivery_man = CustomUser.objects.get(id=delivery_man_id, role='delivery')
            order.delivery_man = delivery_man
            order.save()

            return Response({
                "success": True,
                "statusCode": 200,
                "message": "Delivery man assigned successfully.",
                "data": OrderSerializer(order).data
            })

        except CustomUser.DoesNotExist:
            return Response({
                "success": False,
                "message": "Invalid delivery man ID.",
                "errorDetails": "User with this ID is not a delivery man."
            }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[IsUser])
    def pay(self, request, pk=None):
        order = self.get_object()

        if order.payment_status == 'paid':
            return Response({
                "success": False,
                "message": "Order already paid."
            }, status=400)

        try:
            intent = stripe.PaymentIntent.create(
                amount=5000,  # e.g. 50.00 in paise/cents
                currency='inr',
                metadata={'order_id': order.id},
            )
            order.stripe_payment_id = intent['id']
            order.payment_status = 'paid'
            order.save()

            return Response({
                "success": True,
                "statusCode": 200,
                "message": "Payment successful.",
                "data": {
                    "payment_intent": intent['id'],
                    "client_secret": intent['client_secret']
                }
            })

        except Exception as e:
            return Response({
                "success": False,
                "message": "Payment failed.",
                "errorDetails": str(e)
            }, status=500)