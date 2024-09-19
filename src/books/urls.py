from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .viewsets.borrowing_viewset import BorrowingViewSet
from .viewsets.reservation_viewset import ReservationViewset
from users.viewsets.user_viewset import UserViewSet
from.viewsets.book_viewset import BookViewSet




app_name = 'api'

# Configurer la documentation Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="API documentation for managing students, users, teachers, roles, and addresses",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Créer un routeur pour les viewsets
router = routers.DefaultRouter()
router.register(r'borrow', BorrowingViewSet, basename='borrow')
router.register(r'reservation', ReservationViewset, basename='reservation')
router.register(r'user', UserViewSet, basename='user')
router.register(r'book', BookViewSet, basename='book')






# Définir les URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Inclure les URL du routeur
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # URL pour Swagger
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # URL pour ReDoc (alternative Swagger UI)
]
