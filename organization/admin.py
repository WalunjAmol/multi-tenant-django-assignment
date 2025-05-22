from django.contrib import admin
from organization.models import Organization

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'tenant', 'is_active', 'is_deleted', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('is_active', 'is_deleted', 'tenant')
    readonly_fields = ('created_at', 'updated_at')
