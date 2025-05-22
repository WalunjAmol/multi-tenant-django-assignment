from django.db import models
import uuid

class Tenant(models.Model):
    # Identifiers
    tenant_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="Tenant ID")

    # Basic Info
    name = models.CharField(max_length=255, verbose_name="Tenant Name", blank=False, null=False)
    domain = models.CharField(max_length=255, unique=True, verbose_name="Domain", blank=False, null=False)
    contact_email = models.EmailField(verbose_name="Contact Email", blank=False, null=False)
    logo = models.ImageField(upload_to='tenant_logos/', blank=True, null=True, verbose_name="Logo")
    address = models.TextField(verbose_name="Address", blank=True, null=True)

    # Status Flags
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")


    class Meta:
        verbose_name = "Tenant"
        verbose_name_plural = "Tenants"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.domain})"
