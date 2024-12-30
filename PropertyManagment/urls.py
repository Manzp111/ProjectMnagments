
from django.conf.urls.static import static

# from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView, SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from PropertyManagment import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [


     path('admin/', admin.site.urls),

    path('propertyAPI/', include('PropertyApp.urls')),
    path('',include('core.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(), name='redoc'),

    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    # path('__debug__/', include(debug_toolbar.urls)),
] + debug_toolbar_urls()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

