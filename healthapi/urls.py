from django.contrib import admin
from django.urls import path, include
from core import views
from oauth2_provider.views import TokenView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Include app-specific URLs
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  # OAuth2 Provider URLs
    path('token/', TokenView.as_view(), name='token'),  # Token view for OAuth2
    path('', views.home, name='home'),   # Route for the home view
]

# Add this line to include static files URL patterns
urlpatterns += staticfiles_urlpatterns()
