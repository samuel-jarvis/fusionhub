from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static


urlpatterns = [
    path('', include('pages.urls')),
    path('account/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()