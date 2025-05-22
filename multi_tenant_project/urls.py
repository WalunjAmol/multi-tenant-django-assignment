from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API versioned routing
    path('api/v1/tenants/', include('tenant.urls')),
    path('api/v1/organizations/', include('organization.urls')),
    path('api/v1/departments/', include('department.urls')),
    path('api/v1/customers/', include('customer.urls')),

    # Auth
    path('api/v1/token/', include('core.auth_urls')),
]
