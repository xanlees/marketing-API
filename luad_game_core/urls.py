"""bbi_ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Luad Game API",
        default_version='v1',
        description="Luad Game API ",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="info@luadgame.la"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('', include('user.api.v1.urls'), name='user'),
    path('', include("lottery.api.v1.urls"), name='lottery'),
    path('', include("lottery_time.api.v1.urls"), name='lottery_time'),
    path('', include("lottery_day.api.v1.urls"), name='lottery_day'),
    path('', include("buy_lottery.api.v1.urls"), name='buy_lottery'),
    path('', include("deposit.api.v1.urls"), name='deposit'),
    path('', include("commission.api.v1.urls"), name='commission'),
    path('', include("lottery_product.api.v1.urls"), name='lottery_product'),
    path('', include("lottery_type.api.v1.urls"), name='lottery_type'),
    path('', include("instalment.api.v1.urls"), name='instalment'),




]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
