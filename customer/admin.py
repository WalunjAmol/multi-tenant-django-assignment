from django.contrib import admin
from customer.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'is_active', 'is_deleted', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', 'is_deleted', 'department')
    readonly_fields = ('created_at', 'updated_at')
