
# from django.db import models
from django.db import models
from core.models import User

class Address(models.Model):
    street = models.CharField(max_length=200)
    town = models.CharField(max_length=100)
    house_number = models.IntegerField()

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}-{self.house_number}-{self.town}"

class Landroad(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=200)
    image=models.ImageField(upload_to='landlordProfilePic/',null=True, blank=False)
    def __str__(self):
        return f"{self.user.username}-{self.user.email}-{self.phone}"

class Property(models.Model):
    DoesNotExist = None
    objects = ''
    PROPERTY_TYPES = (
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Car', 'Car'),
        ('Land', 'Land'),
        ('Furniture', 'Furniture'),
        ('Commercial', 'Commercial'),
    )
    owner=models.ForeignKey(Landroad,on_delete=models.CASCADE,null=True,max_length=40)
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address,related_name='property' ,on_delete=models.CASCADE)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    description = models.TextField(blank=True)
    rent = models.DecimalField(max_digits=10, decimal_places=2,default=5000)
    # image =models.ImageField(upload_to='images/', blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.address} - {self.property_type}"
    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images/')
    def __str__(self):
        return f"{self.property.name} - {self.image.name}"



class Unit(models.Model): # price of property
    property = models.ForeignKey(Property, related_name= 'units', on_delete=models.CASCADE)
    unit_count = models.CharField(max_length=15)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.name} - {self.unit_count}"

class Tenant(models.Model): #the renters
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    profile=models.ImageField(upload_to='tenantProfile/')

    def __str__(self):
        return f"{self.user.username} - {self.user.email} - {self.phone_number}"

class Lease(models.Model):
    landroad=models.ForeignKey(Landroad,on_delete=models.CASCADE,null=True)
    tenant = models.ForeignKey(Tenant, related_name='leases', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, related_name='leases', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.unit.is_available} - {self.start_date} - {self.end_date}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} at {self.timestamp}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    created_at = models.DateTimeField(auto_now_add=True)

class MaintenanceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='maintenance_requests')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='maintenance_requests')
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.tenant.user} - {self.status}"


    # Other fields...