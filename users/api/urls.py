from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .users.views import (
    UserViewSet,
    GroupViewSet,
    ContentTypeViewSet,
    DepartmentViewSet,
    PermissionViewSet,
    UsernameFilterView,
    EmailFilterView,
    UserIdDataKeywordFilterView,
    UserNameDataKeywordFilterView,
    UserIdFilterView,
    UserIdKeywordFilterView,
    VendorRolesApi,
    MarketingInchargeFieldApi,
    BrandAnalystFieldApi,
    CheckEmailView,
    CheckUsernameView,
    ImportViewSet,
    ListImportViewSet,
    SearchImportViewSet,
    ExportViewSet,
    SearchExportViewSet,
    ListExportViewSet,
)
from .currency.views import (
    CurrencyViewSet,
    CurrencyFilterView,
    CurrencyIdFilterView,
    CurrencyKeywordFilterView,
    CurrencyFieldApiView
)

schema_view = get_schema_view(openapi.Info(
    title="Users API",
    default_version='v1',
    description="Test description",
), public=True, permission_classes=(permissions.AllowAny,))

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'contenttypes', ContentTypeViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'currency', CurrencyViewSet)
#import & Export
router.register(r'create_import', ImportViewSet)
router.register(r'list_import', ListImportViewSet)
router.register(r'search_import', SearchImportViewSet)

router.register(r'create_export', ExportViewSet)
router.register(r'list_export', ListExportViewSet)
router.register(r'search_export', SearchExportViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('username_filter/', UsernameFilterView.as_view(), name='username_filter'),
    path('check_username/', CheckUsernameView.as_view(), name='check_username'),
    path('check_email/', CheckEmailView.as_view(), name='check_email'),
    path('email_filter/', EmailFilterView.as_view(), name='email_filter'),
    path('userid_filter/', UserIdFilterView.as_view(), name='userid_filter'),
    path('userid_keyword_filter/', UserIdKeywordFilterView.as_view(), name='userid_keyword_filter'),
    path('userid_data_keyword_filter/', UserIdDataKeywordFilterView.as_view(), name='userid_data_keyword_filter'),
    path('username_data_keyword_filter/', UserNameDataKeywordFilterView.as_view(), name='userid_data_keyword_filter'),
    path('currency_filter/', CurrencyFilterView.as_view(), name='currency_filter'),
    path('currencyid_filter/', CurrencyIdFilterView.as_view(), name='currencyid_filter'),
    path('currency_keyword_filter/', CurrencyKeywordFilterView.as_view(), name='currency_keyword_filter'),
    path('vendor_roles_field/', VendorRolesApi.as_view(), name='vendor_roles_field'),
    path('marketing_incharge_field/', MarketingInchargeFieldApi.as_view(), name='marketing_incharge_field'),
    path('brand_analyst_field/', BrandAnalystFieldApi.as_view(), name='brand_analyst_field'),
    path('currency_field/', CurrencyFieldApiView.as_view(), name='currency_field'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
