
from rest_framework import serializers
from .models import  Event, TicketType, Ticket, Payment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'role', 'groups', 'user_permissions']
        
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ['purchase_date', 'code', 'paid']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ['transaction_date', 'status']
