from django.utils.deprecation import MiddlewareMixin
from tenant.models import Tenant
from django.http import JsonResponse

EXCLUDED_PATHS = ['/admin', '/api/v1/token/', '/api/v1/token/refresh/', '/api/v1/tenants/create/']

class TenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if any(request.path.startswith(path) for path in EXCLUDED_PATHS):
            return

        domain = (request.META.get('HTTP_X_TENANT_DOMAIN') or request.get_host().split(":")[0]).strip().lower()
        print(f"[TenantMiddleware] Requested domain: '{domain}'")

        try:
            tenant = Tenant.objects.get(domain__iexact=domain, is_active=True, is_deleted=False)
            request.tenant = tenant
            print("[TenantMiddleware] Tenant resolved:", request.tenant)
        except Tenant.DoesNotExist:
            print(f"[TenantMiddleware] No tenant found for domain: '{domain}'")
            print("Available domains:", list(Tenant.objects.values_list('domain', flat=True)))
            return JsonResponse({"detail": f"Invalid or missing tenant: {domain}"}, status=400)
