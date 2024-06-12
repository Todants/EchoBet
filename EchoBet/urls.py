from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.views import AccountsApi, KeysApi, ListenersApi

router = routers.DefaultRouter()
router.register(r'api/accounts', AccountsApi)
router.register(r'api/keys', KeysApi)
router.register(r'api/listeners', ListenersApi)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
