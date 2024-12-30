from django.conf.urls.static import static
from django.urls import path

from PropertyManagment import settings
from .import views
from PropertyApp.views import PropertySchema,UnitSchema,LeaseSchema,TenantSchema
# from .views import property_list

urlpatterns = [
    path('properties/', views.property_list, name = 'property_list' ),
    path('properties/<int:pk>/', views.property_detail, name= 'property_detail'),

    path('units/', views.unit_list, name = 'unit_list' ),
    path('units/<int:pk>/', views.unit_detail, name= 'unit_detail'),

    path('tenants/', views.tenant_list, name = 'tenant_list' ),
    path('tenants/<int:pk>/', views.tenant_detail, name= 'tenant_detail'),

    path('leases/', views.lease_list, name = 'lease_list' ),
    path('leases/<int:pk>/', views.lease_detail, name= 'lease_detail'),
    path('S.property/',PropertySchema.as_view(), name = 'Property'),
    path('S.unit/',UnitSchema.as_view(), name = 'Unit'),
    path('S.tenant/',TenantSchema.as_view(), name = 'Tenant'),
    path('S.lease/',LeaseSchema.as_view(), name = 'Lease'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)