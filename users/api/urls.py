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
    ListExportViewSet, GetCSVHeaders
)
from .currency.views import (
    CurrencyViewSet,
    CurrencyFilterView,
    CurrencyIdFilterView,
    CurrencyKeywordFilterView,
    CurrencyFieldApiView
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


schema_view = get_schema_view(openapi.Info(
    title="Users API",
    default_version='v1',
    description="Test description",
), public=True, permission_classes=(permissions.AllowAny,))

router = routers.DefaultRouter()
router.register(r'user/users', UserViewSet)
router.register(r'user/groups', GroupViewSet)
router.register(r'user/departments', DepartmentViewSet)
router.register(r'user/contenttypes', ContentTypeViewSet)
router.register(r'user/permissions', PermissionViewSet)
router.register(r'user/currency', CurrencyViewSet)
#import & Export
router.register(r'user/create_import', ImportViewSet, basename='create_import')
router.register(r'user/list_import', ListImportViewSet, basename='list_import')
router.register(r'user/search_import', SearchImportViewSet, basename='search_import')

router.register(r'user/create_export', ExportViewSet, basename='create_export')
router.register(r'user/list_export', ListExportViewSet, basename='list_export')
router.register(r'user/search_export', SearchExportViewSet, basename='search_export')

urlpatterns = [
    path('', include(router.urls)),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/username_filter/', UsernameFilterView.as_view(), name='username_filter'),
    path('user/check_username/', CheckUsernameView.as_view(), name='check_username'),
    path('user/check_email/', CheckEmailView.as_view(), name='check_email'),
    path('user/email_filter/', EmailFilterView.as_view(), name='email_filter'),
    path('user/userid_filter/', UserIdFilterView.as_view(), name='userid_filter'),
    path('user/userid_keyword_filter/', UserIdKeywordFilterView.as_view(), name='userid_keyword_filter'),
    path('user/userid_data_keyword_filter/', UserIdDataKeywordFilterView.as_view(), name='userid_data_keyword_filter'),
    path('user/username_data_keyword_filter/', UserNameDataKeywordFilterView.as_view(), name='userid_data_keyword_filter'),
    path('user/currency_filter/', CurrencyFilterView.as_view(), name='currency_filter'),
    path('user/currencyid_filter/', CurrencyIdFilterView.as_view(), name='currencyid_filter'),
    path('user/currency_keyword_filter/', CurrencyKeywordFilterView.as_view(), name='currency_keyword_filter'),
    path('user/vendor_roles_field/', VendorRolesApi.as_view(), name='vendor_roles_field'),
    path('user/marketing_incharge_field/', MarketingInchargeFieldApi.as_view(), name='marketing_incharge_field'),
    path('user/brand_analyst_field/', BrandAnalystFieldApi.as_view(), name='brand_analyst_field'),
    path('user/currency_field/', CurrencyFieldApiView.as_view(), name='currency_field'),
    path('user/auth/', include('djoser.urls')),
    path('user/auth/', include('djoser.urls.jwt')),
    path("user/docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += path('user/csv/', GetCSVHeaders.as_view(), name="GetCSVHeaders"),
