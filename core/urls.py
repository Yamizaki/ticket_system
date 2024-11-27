from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, TicketTypeViewSet, TicketViewSet, PaymentViewSet, UserViewSet

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('ticket-types', TicketTypeViewSet)
router.register('tickets', TicketViewSet)
router.register('payments', PaymentViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
