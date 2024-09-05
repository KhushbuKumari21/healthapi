from django.contrib import admin
from django.urls import path, include
from core import views
from oauth2_provider.views import TokenView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Include app-specific URLs
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAuth2 Provider URLs
    path('token/', TokenView.as_view(), name='token'),  # Token view for OAuth2
    path('', views.home, name='home'),   # Route for the home view
]

# Add static files URL patterns in development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
