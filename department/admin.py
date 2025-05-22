from django.contrib import admin
from department.models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'organization', 'is_active', 'is_deleted', 'created_at')
    search_fields = ('name', 'code')
    list_filter = ('is_active', 'is_deleted', 'organization')
    readonly_fields = ('created_at', 'updated_at')
