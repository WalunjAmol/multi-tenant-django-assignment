from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from customer.models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated
from department.models import Department

class CustomerListView(ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

  
    def get_queryset(self):
        return Customer.objects.filter(department__organization__tenant=self.request.tenant, is_deleted=False)

class CustomerCreateView(CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        dept_id = self.request.data.get('department_id')
        department = Department.objects.get(id=dept_id, organization__tenant=self.request.tenant)
        serializer.save(department=department)

class CustomerDetailView(RetrieveAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(department__organization__tenant=self.request.tenant)

class CustomerUpdateView(UpdateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(department__organization__tenant=self.request.tenant)

class CustomerDeleteView(DestroyAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(department__organization__tenant=self.request.tenant)
