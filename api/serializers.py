from rest_framework import serializers
from .models import CustomUser, Order

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Auto-fill current user

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['status', 'payment_status', 'stripe_payment_id', 'created_at', 'delivery_man']

