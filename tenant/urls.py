from django.urls import path
from tenant.api.v1.views import (
    TenantListView, TenantCreateView,
    TenantDetailView, TenantUpdateView,
    TenantDeleteView
)

urlpatterns = [
    path('', TenantListView.as_view(), name='tenant-list'),
    path('create/', TenantCreateView.as_view(), name='tenant-create'),
    path('<int:pk>/', TenantDetailView.as_view(), name='tenant-detail'),
    path('<int:pk>/update/', TenantUpdateView.as_view(), name='tenant-update'),
    path('<int:pk>/delete/', TenantDeleteView.as_view(), name='tenant-delete'),
]
