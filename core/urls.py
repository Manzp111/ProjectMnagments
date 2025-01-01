from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
urlpatterns=[
     path('',views.property_view,name='Property'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', views.user_logout, name='logout'),
    path('login/',views.login,name='login'),
    path('home1/ ',views.home1, name='home'),



    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('about/', views.about_view, name='about'),
    path('home/',views. base_view, name='base'),
    path('contact/', views.contact_view, name='contact'),
    path('signup/', views.signup, name='signup'),


    #edit urls

    path('admin1/property/edit/<int:id>/', views.edit_property, name='edit_property'),
    path('user/edit/<int:id>/', views.edit_user, name='edit_user'),
    path('tenant/edit/<int:id>/', views.edit_tenant, name='edit_tenant'),
    path('landroad/edit/<int:id>/', views.edit_landroad, name='edit_landroad'),
    path('unit/edit/<int:id>/', views.edit_unit, name='edit_unit'),
    path('lease/edit/<int:id>/', views.edit_lease, name='edit_lease'),

    #delete urls

    path('property/delete/<int:id>/',views.delete_property, name='delete_property'),
    path('user/delete/<int:id>/', views.delete_user, name='delete_user'),
    path('tenant/delete/<int:id>/', views.delete_tenant, name='delete_tenant'),
    path('landroad/delete/<int:id>/', views.delete_landroad, name='delete_landroad'),
    path('unit/delete/<int:id>/', views.deleteUnit, name='delete_unit'),
    path('lease/delete/<int:id>/', views.delete_lease, name='delete_lease'),

    #add for admin urls

    path('property/landlord/', views.add_property, name='add_property'),
    path('tenant/landlord/', views.add_tenant, name='add_tenant'),
    # path('unit/landlord/', views.add_unit, name='add_unit'),
    path('user/landlord/', views.add_user, name='add_user'),

    # user dashbord

    path('landroad/',views.landroad_dashbord, name='landroad'),
    path('dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
    path('payment/<int:property_id>/', views.process_payment, name='process_payment'),
    path('myProfile/', views.user_profile, name='profile'),
    # path('admin1/', views.admin, name='dashboard'),



    path('messages/<int:receiver_id>/', views.message_board, name='message_board'),
    path('select-receiver/admin/', views.select_receiver, name='select_receiver'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),


    #admin actions
    path('adminD/dashbord/view/', views.dashbord_admin, name='dashbord_admin'),
    path('adminD/property/',views.property_admin, name='property_admin'),
    path('adminD/property/add/',views.add_property_admin, name='add_property_admin'),
    path('adminD/tenants/',views.tenants_admin, name='tenants_admin'),
    path('adminD/tenants/add/',views.add_tenants_admin, name='add_tenants_admin'),
    path('adminD/users/',views.user_admin, name='users_admin_admin'),
    path('adminD/users/add/',views.add_user_admin, name='add_user_admin'),
    path('adminD/lease/',views.lease_admin, name='admin_lease_admin'),
    path('adminD/units/',views.unit_admin, name='units_admin'),
    path('adminD/units/add',views.add_unit_admin, name='add_unit_admin'),
    path('adminD/admin/message/',views.select_receiver_tenant, name='select_receiver_tenant'),
    path('adminD/admin/message/send/<int:receiver_id>/',views.message_board_tenants, name='send_message_tenants'),
    path('send/message/landlord/<int:receiver_id>/',views.message_board_landlord, name='send_message_landlord'),
    path('select_receiver_landlord/',views.select_receiver_landlord, name='select_receiver_landlord'),
    path('properties/landlord/',views.landlord_properties, name='landlord_properties'),
    path('lease/landlord/',views.lease_landlord, name='lease_landlord'),
    path('settings_landlord/',views.landlord_settings,name='settings'),
    path('landlord/admin/',views.landlord_admin, name='landlord_admin'),
    path('adminD/add/landlord/',views.add_landlord, name='add_landlord_admin'),
    path('adminD/edit/photoes/<int:property_id>',views.upload_property_images, name='upload_images'),
    path('landlord/edit/photoes/<int:property_id>',views.upload_property_images_landlord, name='upload_images_landlord'),


    path('submit-request/',views. submit_maintenance_request, name='submit_maintenance_request'),
    # path('view-requests/', views.view_requests, name='view_requests'),
    path('update-request/<int:request_id>/',views. update_request_status, name='update_request_status'),
    path('tenants/request/<int:request_id>',views.view_requests_tenants, name='tenants-result'),

    path('tenant/requests/',views.view_requests_tenants, name='tenant_view_requests'),
    path('landlord/requests/', views.landlord_view_requests, name='landlord_view_requests'),
    path('unit/admin/<int:unit_id>/calendar/', views.availability_calendar, name='availability_calendar'),
    path('unit/<int:unit_id>/availability-data/', views.get_availability_data, name='get_availability_data'),
    path('property/<int:property_id>/images/', views.property_images, name='property_images'),
    path('property/<int:property_id>/images/landlord/', views.property_images_landlord, name='property_images_landlord'),
    path('payment/admin/',views.payment_view, name='payment_admin'),
    # path('payment/landlord/<int:id>', views.payment_landlord_view, name='landlord_payment_landlord'),



    # path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)