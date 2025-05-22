from rest_framework import serializers
from tenant.models import Tenant

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = [
            'id', 'tenant_id', 'name', 'domain',
            'contact_email', 'address', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'tenant_id', 'created_at', 'updated_at']
