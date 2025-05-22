# 🏗 Multi-Tenant Django App

A Django REST API demonstrating a **multi-tenant architecture** with:

✅ Four levels: Tenant → Organization → Department → Customer  
✅ Token-based JWT auth  
✅ API versioning  
✅ Tenant isolation via middleware  
✅ Docker + PostgreSQL ready

---

## Quickstart (Docker)

```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

Admin: http://localhost:8000/admin/

API: Use /api/v1/... endpoints

Auth
Get JWT Token:

POST /api/v1/token/
{
  "username": "admin",
  "password": "admin"
}
Add header to all API requests:

pgsql

Authorization: Bearer <your-token>
X-Tenant-Domain: your-tenant-domain.com
API Routes
Tenant
GET /api/v1/tenants/

POST /api/v1/tenants/create/

etc.

Organization
GET /api/v1/organizations/

etc.

(Repeat for Department, Customer)

# Run Tests

docker-compose exec web python manage.py test
🧰 Tools
Django + DRF

PostgreSQL

Docker

JWT Authentication

URL-based versioning