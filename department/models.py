from django.db import models
from organization.models import Organization

class Department(models.Model):
    # Relationships
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="departments",
        verbose_name="Organization"
    )

    # Basic Info
    name = models.CharField(max_length=255, verbose_name="Department Name")
    code = models.CharField(max_length=50, verbose_name="Department Code")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    # Status Flags
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['name']
        unique_together = ('organization', 'code')

    def __str__(self):
        return f"{self.name} ({self.code})"
