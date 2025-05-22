from django.urls import path
from .api.v1.views import (
    OrganizationListView, OrganizationCreateView,
    OrganizationDetailView, OrganizationUpdateView,
    OrganizationDeleteView
)

urlpatterns = [
    path('', OrganizationListView.as_view(), name='organization-list'),
    path('create/', OrganizationCreateView.as_view(), name='organization-create'),
    path('<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    path('<int:pk>/update/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),
]
