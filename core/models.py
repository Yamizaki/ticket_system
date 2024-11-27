from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid
# Modelo personalizado de Usuario
class User(AbstractUser):
   
    is_staff = models.BooleanField(default=False)
     
    groups = models.ManyToManyField(Group, related_name='user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions')
    
    dni = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    adress = models.CharField(max_length=200)

# Modelo para las experiencias
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Modelo para tipos de entradas
class TicketType(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')

    def __str__(self):
        return self.name

# Modelo para las entradas vendidas
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.event.title} - {self.ticket_type.name}"

# Modelo para los pagos
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=(('completed', 'Completed'), ('pending', 'Pending')))
    transaction_date = models.DateTimeField(auto_now_add=True)
