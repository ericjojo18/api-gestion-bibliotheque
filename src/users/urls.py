from django.contrib import admin
from django.urls import path,re_path,include
from rest_framework import routers
from .viewsets.user_viewsets import UserViewSet
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

app_name = 'users'

schema_view = get_schema_view(
    
        openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Text description",
        terms_of_service="https:/www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@sniper.local"),
        livences=openapi.License(name="BSD Licence"),
    ),
        public=True,
        permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    
    re_path(r'^swagger(?P<format>\.json|\.yanL)$', schema_view.without_ui(cache_timeout=0), name='shema-json'),
    re_path(r'swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]