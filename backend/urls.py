
from django.urls import path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="APIs",
        default_version='v1',
        description="Api Docs",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('user.urls', 'user'), namespace='user')),
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
    #      name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
]
