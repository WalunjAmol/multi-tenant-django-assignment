from django.urls import path
from .api.v1.views import (
    DepartmentListView, DepartmentCreateView,
    DepartmentDetailView, DepartmentUpdateView,
    DepartmentDeleteView
)

urlpatterns = [
    path('', DepartmentListView.as_view(), name='department-list'),
    path('create/', DepartmentCreateView.as_view(), name='department-create'),
    path('<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('<int:pk>/update/', DepartmentUpdateView.as_view(), name='department-update'),
    path('<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),
]
