from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from department.models import Department
from .serializers import DepartmentSerializer
from rest_framework.permissions import IsAuthenticated

class DepartmentListView(ListAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.filter(
            organization__tenant=self.request.tenant,
            is_deleted=False
        )

class DepartmentCreateView(CreateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        org_id = self.request.data.get('organization_id')
        from organization.models import Organization
        organization = Organization.objects.get(id=org_id, tenant=self.request.tenant)
        serializer.save(organization=organization)

class DepartmentDetailView(RetrieveAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.filter(organization__tenant=self.request.tenant)

class DepartmentUpdateView(UpdateAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.filter(organization__tenant=self.request.tenant)

class DepartmentDeleteView(DestroyAPIView):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Department.objects.filter(organization__tenant=self.request.tenant)
