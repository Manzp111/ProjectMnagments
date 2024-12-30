
from django.contrib import admin
from .models import Property, Unit, Tenant, Lease,Address,Landroad,Payment,Message,PropertyImage,MaintenanceRequest
admin.site.site_header ="Property Management Service"
admin.site.index_title = "Property Management App"

@admin.register(Landroad)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'phone')

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'property_type', 'address', 'description')
    search_fields = ('id', 'name', 'property_type')

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('id','property', 'unit_count', 'bedrooms', 'bathrooms', 'is_available')
    list_filter = ('property', 'unit_count')
    search_fields = ('unit_count', 'bedrooms', 'bathrooms')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'unit', 'start_date', 'end_date', 'rent_amount')
    search_fields = ('start_date','end_date')
    list_filter = ('start_date', 'end_date')
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street','house_number')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender','receiver','content')

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'image')


@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'property', 'tenant', 'description', 'status')


