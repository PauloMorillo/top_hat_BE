from discussion.views import DiscussionQuestionViewSet
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'discussion_question', DiscussionQuestionViewSet, basename="discussion_question")

schema_view = get_schema_view(
    openapi.Info(
        title="Top Hat BE Discussion Question API",
        default_version='v1',
        description="This is a test only to show a tree structure for a discussion question API",
        terms_of_service="https://www.github.com/PauloMorillo/",
        contact=openapi.Contact(email="paulomorillo@globant.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
