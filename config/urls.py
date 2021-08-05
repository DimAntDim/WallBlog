from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wall_common.urls')),
    path('account/', include('wall_auth.urls')),
    path('profile/', include('wall_profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

