from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core import views

router = DefaultRouter()
router.register(r"points", views.PointView, basename="point")
urlpatterns = router.urls

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns += [
    path("register/client", views.client_register, name="register"),
    path("login/client", views.client_login, name="login"),
    path('email/', views.email_getter, name='emails_getter'),
    re_path(r"find/(?P<name>\w+)/", views.point_finder, name="find_by_name"),
    re_path(
        "swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
