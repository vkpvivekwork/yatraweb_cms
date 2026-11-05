from django.urls import path
from .views import BookingCreateView, BookingAdminListView, BookingAdminDetailView

urlpatterns = [
    path('', BookingCreateView.as_view(), name='booking-create'),
    path('admin/', BookingAdminListView.as_view(), name='booking-admin-list'),
    path('admin/<int:pk>/', BookingAdminDetailView.as_view(), name='booking-admin-detail'),
]
