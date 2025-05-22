from django.db import models
from tenant.models import Tenant

class Organization(models.Model):
    # Relationships
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name="organizations",
        verbose_name="Tenant"
    )

    # Basic Info
    name = models.CharField(max_length=255, verbose_name="Organization Name")
    code = models.CharField(max_length=50, verbose_name="Organization Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    logo = models.ImageField(upload_to='organization_logos/', blank=True, null=True, verbose_name="Logo")

    # Status Flags
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ['name']
        unique_together = ('tenant', 'code')

    def __str__(self):
        return f"{self.name} ({self.code})"
