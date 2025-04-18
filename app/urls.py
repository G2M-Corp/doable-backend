from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from uploader.router import router as uploader_router
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import UserViewSet, TarefaViewSet, CategoriaViewSet

router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"tarefas", TarefaViewSet, basename="tarefas")
router.register(r"categorias", CategoriaViewSet, basename="categorias")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/media/", include(uploader_router.urls)),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # API
    path("api/", include(router.urls)),

    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
