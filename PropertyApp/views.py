# from django.shortcuts import render
from .models import Property, Unit, Tenant, Lease
from .serializers import PropertySerializer, UnitSerializer, TenantSerializer, LeaseSerializer
from rest_framework.decorators import api_view , permission_classes
from  rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


@extend_schema(
    methods=["GET"],
    responses={200: PropertySerializer(many=True)},
    description="List of all properties",
)
@extend_schema(
    methods=["POST"],
    responses={201: PropertySerializer},
    description=" properties created successfully",
)
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes([])
def property_list(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    methods=["GET"],
    responses={200: PropertySerializer(many=True)},
    description="List of all properties",
)
@extend_schema(
    methods=["POST"],
    responses={201: PropertySerializer},
    description=" properties created successfully",
)
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def property_detail(request, pk):
    try:
        properties = Property.objects.get(pk=pk)

    except Property.DoesNotExist:
        return Response(['error : property not Found'], status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = PropertySerializer(properties)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PropertySerializer(properties, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        properties.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(
    methods=["GET"],
    responses={200: UnitSerializer(many=True)},
    description="retrieve of all properties",
)
@extend_schema(
    methods=["POST"],
    responses={201: UnitSerializer},
    description="updating of all properties",
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def unit_list(request):
    if request.method == 'GET':
      units = Unit.objects.all()
      serializer = UnitSerializer(units, many = True)
      return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = UnitSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#unit views
@extend_schema(
    methods=["GET"],
    responses={200: UnitSerializer(many=True)},
    description="List of all units",
)
@extend_schema(
    methods=["POST"],
    responses={201: UnitSerializer},
    description=" units created successfully",
)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def unit_detail(request, pk):
    try:
        units = Unit.objects.get(pk=pk)
    except Unit.DoesNotExist:
        return Response(['error : unit not Found'], status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UnitSerializer(units)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UnitSerializer(units, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        units.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#tenant views

@extend_schema(
    methods=["GET"],
    responses={200: TenantSerializer(many=True)},
    description="List of all Tenants",
)
@extend_schema(
    methods=["POST"],
    responses={201: TenantSerializer},
    description="Tenant created successfully",
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tenant_list(request):
    if request.method == 'GET':
        tenants = Tenant.objects.all()
        serializer = TenantSerializer(tenants, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TenantSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    methods=["GET"],
    responses={200: TenantSerializer(many=True)},
    description="list of all Tenants ",
)
@extend_schema(
    methods=["POST"],
    responses={201: TenantSerializer},
    description="tenant created successfully",
)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tenant_detail(request, pk):
    try:
        tenants = Tenant.objects.get(pk = pk)

    except Tenant.DoesNotExist:
        return Response(['error : tenant not Found'], status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
           serializer = TenantSerializer(tenants)
           return Response(serializer.data)
    elif request.method == 'PUT':
           serializer = TenantSerializer(tenants, data = request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(status=status.HTTP_201_CREATED)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
           tenants.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)

#lease views
@extend_schema(
    methods=["GET"],
    responses={200: LeaseSerializer(many=True)},
    description="List of all leases",
)
@extend_schema(
    methods=["POST"],
    responses={201: LeaseSerializer},
    description="leases created successfully",
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lease_list(request):
    if request.method == 'GET':
        leases = Lease.objects.all()
        serializer = LeaseSerializer(leases, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LeaseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    methods=["GET"],
    responses={200: LeaseSerializer(many=True)},
    description="List of all leases",
)
@extend_schema(
    methods=["POST"],
    responses={201: LeaseSerializer},
    description="Leases retrieved successfully",
)
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def lease_detail(request, pk):
    try:
        leases = Lease.objects.get(pk = pk)
    except Lease.DoesNotExist:
        return Response(['error : lease not Found'], status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeaseSerializer(leases, many = True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LeaseSerializer(leases, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        leases.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class PropertySchema(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]
class UnitSchema(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [permissions.IsAuthenticated]
class TenantSchema(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [permissions.IsAuthenticated]
class  LeaseSchema(generics.ListCreateAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [permissions.IsAuthenticated]

