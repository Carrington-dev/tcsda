from django.contrib import admin
from django.urls import path, include
from softyweb import settings
from django.conf.urls.static import static

version = 'v1'

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),

    path(f'api/{ version }/auth/', include('djoser.urls')),
    path(f"api/{ version }/auth/", include("djoser.urls.jwt")),
    path(f"api/{ version }/transactions/", include("transact.urls")),
    # path('api/v1/auth/', include('djoser.urls.authtoken')),
]

admin.site.site_title = "Tshwane Central SDA Church Services"
admin.site.site_header = "Tshwane Central SDA Church Org"
admin.site.index_title = "Tshwane Central SDA Church welcomes you!!!"


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)