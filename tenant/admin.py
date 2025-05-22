from django.contrib import admin
from tenant.models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'contact_email', 'is_active', 'is_deleted', 'created_at')
    search_fields = ('name', 'domain', 'contact_email')
    list_filter = ('is_active', 'is_deleted')
    readonly_fields = ('tenant_id', 'created_at', 'updated_at')
