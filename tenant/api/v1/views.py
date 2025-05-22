from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
)
from tenant.models import Tenant
from .serializers import TenantSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TenantListView(ListAPIView):
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Tenant.objects.filter(id=self.request.tenant.id)

class TenantCreateView(CreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TenantDetailView(RetrieveAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TenantUpdateView(UpdateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TenantDeleteView(DestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
