
from rest_framework import serializers
from .models import Property, Unit, Tenant, Lease

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('id', 'name', 'address', 'description', 'property_type', 'number_of_units')
        read_only_fields = ('id', )

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'property', 'unit_count', 'bedrooms', 'bathrooms', 'rent', 'is_available')


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ('id', 'name', 'email', 'phone_number')

class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = ('id', 'tenant', 'unit', 'start_date', 'end_date', 'rent_amount')
