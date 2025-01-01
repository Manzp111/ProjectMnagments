from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from PropertyApp.form import ContactForm, MessageForm
from  core.forms import *
from core.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta
from datetime import timedelta
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from PropertyApp.models import Message, Tenant, Landroad,Unit
from django.db.models import Sum
import stripe
from PropertyApp.models import Property,Payment,PropertyImage
from django.conf import settings
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from core.models import User
from django.utils import timezone

from .forms import UserForm






def home1(request):
    return render(request, 'home.html')



def about_view(request):
    return render(request,'Property/about.html')



@login_required
def base_view(request):
    try:
        tenant = Tenant.objects.get(user=request.user)  # Retrieve the tenant linked to the logged-in user
        leases = Lease.objects.filter(tenant=tenant)  # Filter leases related to the tenant
    except Tenant.DoesNotExist:
        tenant = None
        leases = []

    return render(request, 'base.html', {'tenants': tenant, 'leases': leases})

def contact_view(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Property')
    form=ContactForm()
    return render(request,'Property/contact.html' ,{'contact_forms':form})





def signup(request):
    if request.method=='POST':
       form=UserForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('login')

    else:
     form = UserForm()
    return render(request, 'forms/createAccount.html', {'form': form})

def property_images(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    images = property_instance.images.all()  # Assuming related_name='images' in PropertyImage model

    return render(request, 'edit/editPropertyImage.html', {
        'property': property_instance,
        'images': images,
    })
def property_images_landlord(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)
    images = property_instance.images.all()  # Assuming related_name='images' in PropertyImage model

    return render(request, 'landlord/landlord_add_image.html', {
        'property': property_instance,
        'images': images,
    })
def edit_property(request, id):
    property_instance = get_object_or_404(Property, id=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('property_admin')  # Redirect to the dashboard or another page
        else:
            print(form.errors)  # Debugging: print form errors if any
    else:
        form = PropertyForm(instance=property_instance)

    return render(request, 'edit/editp.html', {'form': form})

def edit_property_landlord(request, id):
    property_instance = get_object_or_404(Property, id=id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('landlord_properties')  # Redirect to the dashboard or another page
        else:
            print(form.errors)  # Debugging: print form errors if any
    else:
        form = PropertyForm(instance=property_instance)

    return render(request, 'landlord/editp.html', {'form': form})


def edit_user(request,id):
    user_instance = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserFormEdit(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            return redirect('users_admin_admin')  # Redirect to the dashboard or another page
    else:
        form = UserFormEdit(instance=user_instance)
    return render(request, 'edit/editUser.html', {'form': form})

def edit_tenant(request, id):
    tenant_instance = get_object_or_404(Tenant, id=id)
    if request.method == 'POST':
        form = TenantForm(request.POST, instance=tenant_instance)
        if form.is_valid():
            form.save()
            return redirect('tenants_admin')  # Redirect to the dashboard or another page
    else:
        form = TenantForm(instance=tenant_instance)
    return render(request, 'edit/editTenant.html', {'form': form})

def edit_unit(request, id):
    unit_instance = get_object_or_404(Unit, id=id)
    if request.method == 'POST':
        form = UnitForm(request.POST, instance=unit_instance)
        if form.is_valid():
            form.save()
            return redirect('units_admin')  # Redirect to the dashboard or another page
    else:
        form = UnitForm(instance=unit_instance)
    return render(request, 'edit/editUnit.html', {'form': form})

def edit_lease(request, id):
    lease_instance = get_object_or_404(Lease, id=id)
    if request.method == 'POST':
        form = LeaseForm(request.POST, instance=lease_instance)
        if form.is_valid():
            form.save()
            return redirect('admin_lease_admin')  # Redirect to the dashboard or another page
    else:
        form = LeaseForm(instance=lease_instance)
    return render(request, 'edit/editLease.html', {'form': form})

def edit_landroad(request, id):
    landroad_instance = get_object_or_404(Landroad, id=id)
    if request.method == 'POST':
        form = LandroadForm(request.POST, instance=landroad_instance)
        if form.is_valid():
            form.save()
            return redirect('add_landlord_admin')  # Redirect to the dashboard or another page
    else:
        form = LandroadForm(instance=landroad_instance)
    return render(request, 'edit/editLandroad.html', {'form': form})



def delete_property(request, id):
    # Get the property instance
    property_instance = get_object_or_404(Property, id=id)

    if request.method == 'POST':  # Handle POST request to delete
        property_instance.delete()
        return redirect('property_admin')  # Redirect after deletion

    # If it's a GET request, render the confirmation page
    return render(request, 'delete/delete.html', {'object': property_instance})





def delete_user(request, id):
    user_instance = get_object_or_404(User, id=id)
    if request.method == 'POST':  # Confirm deletion with a POST request
        user_instance.delete()
        return redirect('users_admin_admin')  # Redirect to the dashboard or another page
    return render(request, 'delete/deleteuser.html', {'object': user_instance})
def delete_tenant(request, id):
    tenant_instance = get_object_or_404(Tenant, id=id)
    if request.method == 'POST':  # Confirm deletion with a POST request
        tenant_instance.delete()
        return redirect('tenants_admin')  # Redirect to the dashboard or another page
    return render(request, 'delete/deleteTenant.html', {'object': tenant_instance})

def deleteUnit(request, id):
    unit_instance = get_object_or_404(Unit, id=id)
    if request.method == 'POST':  # Confirm deletion with a POST request
        unit_instance.delete()
        return redirect('units_admin')  # Redirect to the dashboard or another page
    return render(request, 'delete/deleteUnit.html', {'object': unit_instance})

def delete_lease(request, id):
    lease_instance = get_object_or_404(Lease, id=id)
    if request.method == 'POST':  # Confirm deletion with a POST request
        lease_instance.delete()
        return redirect('admin_lease_admin')  # Redirect to the dashboard or another page
    return render(request, 'delete/deleteLease.html', {'object': lease_instance})

def delete_landroad(request, id):
    landroad_instance = get_object_or_404(Landroad, id=id)
    if request.method == 'POST':  # Confirm deletion with a POST request
        landroad_instance.delete()
        return redirect('landlord_admin')  # Redirect to the dashboard or another page
    return render(request, 'delete/deleteLandroad.html', {'object': landroad_instance})


def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
        else:
            print(form.errors)
    else:
        form = PropertyForm()
    return render(request, 'landlord/addProperty.html', {'form': form})
def add_landlord(request):
    if request.method == 'POST':
        form = LandroadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landlord_admin')
        else:
            print(form.errors)
    else:
        form = LandroadForm()
    return render(request, 'admin/addLandroad.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Or to another page
    else:
        form = UserForm()
    return render(request, 'landlord/addUser.html', {'form': form})

def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Or to another page
    else:
        form = TenantForm()
    return render(request, 'landlord/addTenant.html', {'form': form})







@login_required
def landroad_dashbord(request):
    try:
        landroad_instance = Landroad.objects.get(user=request.user)
    except Landroad.DoesNotExist:
        landroad_instance = None

    if landroad_instance:
        properties = Property.objects.filter(owner=landroad_instance)
        leases = Lease.objects.filter(landroad=landroad_instance)

        # Calculate total rent amount
        total_rent = leases.aggregate(total_rent=Sum('rent_amount'))['total_rent'] or 0
    else:
        properties = []
        leases = []
        total_rent = 0

    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return render(request, 'landlord/dashbord.html', {
        'landroad_instance': landroad_instance,
        'properties': properties,
        'leases': leases,
        'greeting': greeting,
        'total_rent': total_rent,  # Pass the total rent amount to the template
    })

# def myProfile(request):
#
#     return render(request, 'edit/myprofile.html')

@login_required
def user_profile(request):
    user = request.user  # Get the currently logged-in user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            if user.user_type == 'Tenants':
              return redirect('tenant_dashboard')
            elif user.user_type == 'Landlord':
              return redirect('landlord_dashboard')
    else:
        form = UserProfileForm(instance=user)  # Pre-fill the form with the user's current data

    return render(request, 'edit/myprofile.html', {
        'form': form,
    })

def tenant_dashboard(request):
    # Get the tenant for the logged-in user
    tenant = Tenant.objects.get(
        user=request.user)  # Assumes Tenant model has a OneToOne relationship with the User model

    # Fetch all leases for the tenant
    leases = Lease.objects.filter(tenant=tenant)

    # Check if the tenant has any leases
    if not leases.exists():  # If no leases exist
        messages.warning(request, "You don't have any leases. Redirecting to the property home.")
        return redirect('Property')  # Replace 'Property' with your actual home URL name

    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    context = {
        'tenant': tenant,
        'leases': leases,
        'greeting': greeting,
    }

    return render(request, 'Property/tenants.html', context)


@login_required
def message_board(request, receiver_id):
    receiver = User.objects.get(pk=receiver_id)
    # Fetch all messages between the sender and receiver

    if request.method == "POST":
        # Create a new message
        content = request.POST['content']
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('message_board', receiver_id=receiver.id)

    # Fetch all messages between the sender and receiver
    messages = Message.objects.filter(
        sender=request.user, receiver=receiver
    ) | Message.objects.filter(
        sender=receiver, receiver=request.user
    ).order_by('timestamp')

    return render(request, 'forms/send_message.html', {
        'receiver': receiver,
        'messages': messages
    })


@login_required
def select_receiver(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    search_query = request.GET.get('search', '')

    if search_query:
        users = users.filter(username__icontains=search_query)

    for user in users:
        # Get the last message sent to the user or from the user
        last_message = Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by('-timestamp').first()

        # Add the last message and its read status to each user
        user.last_message = last_message

    # Check for AJAX request using the 'X-Requested-With' header
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # If it's an AJAX request, return the rendered HTML of the user list
        return render(request, 'forms/user_list_partial.html', {'users': users})

    # If it's a normal request, render the full page
    return render(request, 'forms/lanlordmessage.html', {'users': users})

def property_detail(request,pk):
    property = get_object_or_404(Property, pk=pk)
    units = Unit.objects.filter(property=property)  # This should filter correctly



    return render(request, 'Property/property_detail.html', {
        'property': property,
        'units': units,
    })


# Stripe test keys
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY



def process_payment(request, property_id):
    property = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        # Ensure the tenant exists or create one if not
        tenant = Tenant.objects.filter(user=request.user).first()
        if not tenant:
            tenant = Tenant.objects.create(user=request.user)

        # Parse start and end dates
        start_date = timezone.datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = timezone.datetime.strptime(end_date_str, '%Y-%m-%d').date()

        # Calculate rent amount based on the number of days
        total_days = (end_date - start_date).days
        rent_amount = total_days * property.rent

        try:
            # Process the payment with Stripe
            charge = stripe.Charge.create(
                amount=int(rent_amount * 100),  # Amount in cents
                currency='usd',
                description=f'Rent for {property.name}',
                source=token,
            )

            # Create a lease for the tenant and property unit
            unit = get_object_or_404(Unit, property=property, is_available=True)

            lease = Lease.objects.create(
                landroad=property.owner,   # Landlord is the property owner
                tenant=tenant,             # Tenant is the logged-in user
                unit=unit,                 # The unit they are renting
                start_date=start_date,     # Use the start date from the form
                end_date=end_date,         # Use the end date from the form
                rent_amount=rent_amount     # Use the calculated rent amount
            )

            # Update unit availability
            unit.is_available = False
            unit.save()

            # Create the payment record in the database
            Payment.objects.create(
                user=request.user,
                property=property,
                amount=rent_amount,  # Use the calculated rent amount
                status='Completed'
            )

            # Success message and redirect to tenant dashboard
            messages.success(request, "Payment successful! Lease created.")
            return redirect('tenant_dashboard')  # Redirect to tenant dashboard

        except stripe.error.StripeError as e:
            # Handle payment error
            messages.error(request, f"Error processing payment: {e}")
            return redirect('process_payment', property_id=property.id)  # Stay on the payment page

    return render(request, 'forms/payment.html', {
        'property': property,
        'stripe_public_key': settings.STRIPE_TEST_PUBLIC_KEY,  # Pass Stripe public key to the template
    })

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.user_type == 'Tenants':
                    try:
                        tenant = Tenant.objects.get(user=user)
                        leases = Lease.objects.filter(tenant=tenant)
                        if not leases.exists():  # No leases found
                            messages.warning(request,
                                             f"Dear {tenant.user.username}, no lease agreement found. Please rent a property.")
                            return redirect('Property')  # Redirect to property home
                    except Tenant.DoesNotExist:
                        messages.error(request, "Tenant profile not found please rent an property.")
                        return redirect('login')
                    return redirect('tenant_dashboard')  # Redirect to tenant dashboard
                elif user.user_type == 'Admin':
                    return redirect('dashbord_admin')
                elif user.user_type == 'Landroad':
                    return redirect('landroad')
                else:
                    messages.error(request, "You are not recognized.")
                    return redirect('login')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('login')

    return render(request, 'forms/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Property')

def tenant_message(request):
    return render(request, 'message/messageTenants.html')



def add_property_admin(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('property_admin')
        else:
            print(form.errors)
    else:
        form = PropertyForm()
    return render(request, 'admin/addProperty.html', {'form': form})

# def property_admin(request,property_id):
#     properties =  Property.objects.get(id=property_id)
#     Property_image=properties.images.all()
#
#     return render(request, 'admin/Property.html',{
#         "property": properties,
#         "property_image": Property_image,
#                                  })
def property_admin(request):
    properties=Property.objects.all()


    return render(request, 'admin/Property.html', {
        "property": properties,

    })

def tenants_admin(request):
    tenant = Tenant.objects.all()
    return render(request, 'admin/tenants.html',{  "tenants": tenant,})

def add_tenants_admin(request):
    if request.method == 'POST':
        form = TenantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tenants_admin')  # Or to another page
    else:
        form = TenantForm()
    return render(request, 'admin/addTenant.html', {'form': form})
def user_admin(request):
    user = User.objects.all()
    return render(request, 'admin/user.html',{"users":user,})

def add_user_admin(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users_admin_admin')  # Or to another page
    else:
        form = UserForm()
    return render(request, 'admin/addUser.html', {'form': form})

def lease_admin(request):
    lease = Lease.objects.all()
    return render(request, 'admin/lease.html', {'lease': lease})

def unit_admin(request):
    units = Unit.objects.all()
    return render(request, 'admin/units.html', {'units': units})


def add_unit_admin(request):
    if request.method == 'POST':
        form = UnitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('units_admin')  # Or to another page
    else:
        form = UnitForm()
    return render(request, 'admin/addUnits.html', {'form': form})

@login_required
def select_receiver_tenant(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    search_query = request.GET.get('search', '')

    if search_query:
        users = users.filter(username__icontains=search_query)

    for user in users:
        # Get the last message sent to the user or from the user
        last_message = Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by('-timestamp').first()
        user.last_message = last_message
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # If it's an AJAX request, return the rendered HTML of the user list
        return render(request, 'message/user_list_partial.html', {'users': users})
    return render(request, 'message/messageTenants.html', {'users': users})

@login_required
def message_board_tenants(request, receiver_id):
    receiver = User.objects.get(pk=receiver_id)
    # Fetch all messages between the sender and receiver

    if request.method == "POST":
        # Create a new message
        content = request.POST['content']
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('send_message_tenants', receiver_id=receiver.id)

    # Fetch all messages between the sender and receiver
    messages = Message.objects.filter(
        sender=request.user, receiver=receiver
    ) | Message.objects.filter(
        sender=receiver, receiver=request.user
    ).order_by('timestamp')

    return render(request, 'message/send_message.html', {
        'receiver': receiver,
        'messages': messages
    })
@login_required
def select_receiver_landlord(request):
    users = User.objects.exclude(id=request.user.id)  # Exclude the current user
    search_query = request.GET.get('search', '')

    if search_query:
        users = users.filter(username__icontains=search_query)

    for user in users:
        # Get the last message sent to the user or from the user
        last_message = Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).order_by('-timestamp').first()
        user.last_message = last_message
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # If it's an AJAX request, return the rendered HTML of the user list
        return render(request, 'landlord/user_list_partial.html', {'users': users})
    return render(request, 'landlord/messageTenants.html', {'users': users})

@login_required
def message_board_landlord(request, receiver_id):
    receiver = User.objects.get(pk=receiver_id)
    # Fetch all messages between the sender and receiver

    if request.method == "POST":
        # Create a new message
        content = request.POST['content']
        Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('send_message_landlord', receiver_id=receiver.id)

    # Fetch all messages between the sender and receiver
    messages = Message.objects.filter(
        sender=request.user, receiver=receiver
    ) | Message.objects.filter(
        sender=receiver, receiver=request.user
    ).order_by('timestamp')

    return render(request, 'landlord/send_message.html', {
        'receiver': receiver,
        'messages': messages
    })
def landlord_properties(request):
    try:
        landroad_instance = Landroad.objects.get(user=request.user)
    except Landroad.DoesNotExist:
        landroad_instance = None

    if landroad_instance:
        properties = Property.objects.filter(owner=landroad_instance)

    else:
        properties = []


    return render(request, 'landlord/properties.html', {
        'properties': properties
    })
def lease_landlord(request):
    try:
        landroad_instance = Landroad.objects.get(user=request.user)
    except Landroad.DoesNotExist:
        landroad_instance = None

    if landroad_instance:

        leases = Lease.objects.filter(landroad=landroad_instance)

    else:
        properties = []
        leases = []
    return render(request, 'landlord/lease.html', {'leases': leases})


def landlord_settings(request):
    return render(request, 'landlord/setting.html')




def landlord_admin(request):
    landlords = Landroad.objects.all()

    for landlord in landlords:
        # Count properties owned by the landlord
        landlord.num_properties = Property.objects.filter(owner=landlord).count()

        # Count leases associated with the landlord
        landlord.num_leases = Lease.objects.filter(landroad=landlord).count()

    context = {
        'landlords': landlords,
    }

    return render(request, 'admin/landlordList.html', context)

def dashbord_admin(request):
    """Render the admin dashboard template."""
    # Fetch metrics directly for rendering
    total_properties = Property.objects.count()
    total_users = Tenant.objects.count()
    total_landlords = Landroad.objects.count()
    active_leases = Lease.objects.filter(landroad__isnull=False).count()

    total_units = Unit.objects.count()
    occupied_units = Unit.objects.filter(is_available=False).count()
    occupancy_rate = (occupied_units / total_units * 100) if total_units > 0 else 0

    total_revenue = Payment.objects.aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'total_properties': total_properties,
        'total_users': total_users,
        'total_landlords': total_landlords,
        'active_leases': active_leases,
        'occupancy_rate': occupancy_rate,
        'total_revenue': total_revenue,
    }

    return render(request, 'admin/dashbord.html', context)



def property_view(request):
    properties = Property.objects.all()  # Start with all properties

    # Get the search query from the request
    search_query = request.GET.get('search', '')

    # Filter based on the search input
    if search_query:
        # Split the query into keywords for flexible searching
        keywords = search_query.split()
        query = Q()

        # Build the query dynamically using the Address model fields
        for keyword in keywords:
            query |= (
                Q(address__street__icontains=keyword) |  # Search by street in the address
                Q(address__town__icontains=keyword) |  # Search by town in the address
                Q(property_type__icontains=keyword) |
                Q(units__bedrooms__icontains=keyword) |  # Assuming this field is used for bedrooms
                Q(rent__icontains=keyword)  # Assuming this is for price
            )

        properties = properties.filter(query)

    # Get the current hour for greeting
    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    # Return the properties and greeting to the template
    return render(request, 'Property/Property.html', {
        'properties': properties,
        'search': search_query,
        'greeting': greeting,
    })

def upload_property_images(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        images = request.FILES.getlist('images')

        # Validate number of images
        if len(images) < 2:
            return render(request, 'admin/addImage.html', {
                'property': property_instance,
                'error_message': "Please upload at least 2 images."
            })

        # Save the images if validation passes
        for image in images:
            property_image = PropertyImage(property=property_instance, image=image)
            property_image.save()

        return redirect('property_images',property_id=property_id)  # Adjust as needed

    return render(request, 'admin/addImage.html', {
        'property': property_instance,
    })

def upload_property_images_landlord(request, property_id):
    property_instance = get_object_or_404(Property, id=property_id)

    if request.method == 'POST':
        images = request.FILES.getlist('images')

        # Validate number of images
        if len(images) < 2:
            return render(request, 'admin/addImage.html', {
                'property': property_instance,
                'error_message': "Please upload at least 2 images."
            })

        # Save the images if validation passes
        for image in images:
            property_image = PropertyImage(property=property_instance, image=image)
            property_image.save()

        return redirect('property_images_landlord',property_id=property_id)  # Adjust as needed

    return render(request, 'landlord/add_image_landlord.html', {
        'property': property_instance,
    })

def view_requests_tenants(request):
    if request.user.is_authenticated:
        tenant = get_object_or_404(Tenant, user=request.user)
        requests = MaintenanceRequest.objects.filter(tenant=tenant)
        return render(request, 'Property/result_maintanance_tenants.html', {'requests': requests})
    else:
        return redirect('login')

@login_required
def update_request_status(request, request_id):
    maintenance_request = get_object_or_404(MaintenanceRequest, id=request_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        maintenance_request.status = new_status
        maintenance_request.save()
        return redirect('landlord_view_requests')

    return render(request, 'landlord/update_requests.html', {'request': maintenance_request})

@login_required
def submit_maintenance_request(request):
    if request.user.is_authenticated:
        tenant = get_object_or_404(Tenant, user=request.user)
        if request.method == 'POST':
            property_id = request.POST.get('property_id')  # Assuming you pass this from the form
            description = request.POST.get('description')
            property_instance = get_object_or_404(Property, id=property_id)

            # Create the maintenance request
            MaintenanceRequest.objects.create(
                tenant=tenant,
                property=property_instance,
                description=description
            )
            return redirect('tenant_view_requests')  # Redirect to a success page

        properties = Property.objects.all()  # Fetch properties for the form
        return render(request, 'Property/submit_requests.html', {'properties': properties})
    else:
        return redirect('login')
def landlord_view_requests(request):
    if request.user.is_authenticated:
        try:
            landlord = Landroad.objects.get(user=request.user)  # Get the logged-in landlord
            properties = Property.objects.filter(owner=landlord)# Get properties owned by the landlord
            requests = MaintenanceRequest.objects.filter(property__in=properties)  # Get requests for those properties
            return render(request, 'landlord/view_requests_landlord.html', {'requests': requests})
        except Landroad.DoesNotExist:
            return HttpResponse("no maintanace requests for your property")  # Handle if no landlord found
    else:
        return redirect('login')  # Redirect to login if not authenticated

def availability_calendar(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    return render(request, 'admin/admin_calendar.html', {
        'unit': unit,
    })

def get_availability_data(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    leases = unit.leases.all()  # Assuming you have a reverse relationship from Lease to Unit

    events = []
    for lease in leases:
        events.append({
            'title': 'Unavailable',
            'start': lease.start_date.isoformat(),
            'end': lease.end_date.isoformat(),
            'rendering': 'background',  # Render as background
        })

    return JsonResponse(events, safe=False)
def payment_view(request):
    payments=Payment.objects.all()
    return render(request, 'admin/payment.html', {'payments': payments})

# def payment_landlord_view(request,id):
#
#         landlord = get_object_or_404(user=request.user)  # Get the logged-in landlord
#         payments = Payment.objects.filter(id=landlord)  # Get payments for the landlord
#         return render(request, 'landlord/payment_landlord.html', {'payments': payments})