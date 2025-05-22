from django.db import models
from department.models import Department

class Customer(models.Model):
    # Relationships
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="customers",
        verbose_name="Department"
    )

    # Basic Info
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    email = models.EmailField(verbose_name="Email", unique=True)
    phone = models.CharField(max_length=20, verbose_name="Phone", blank=True, null=True)
    address = models.TextField(verbose_name="Address", blank=True, null=True)

    # Status Flags
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
