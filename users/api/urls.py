from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view
from .users.views import (
	UserViewSet,
	GroupViewSet,
	ContentTypeViewSet,
	DepartmentViewSet,
	PermissionViewSet,
	UsernameFilterView,
	EmailFilterView,
	UserIdDataKeywordFilterView,
	UserIdFilterView,
	UserIdKeywordFilterView,
	VendorRolesApi
)
from .currency.views import (
	CurrencyViewSet,
	CurrencyFilterView,
	CurrencyIdFilterView,
	CurrencyKeywordFilterView
)


schema_view = get_swagger_view(title='Micromerce API')
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'contenttypes', ContentTypeViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'currency', CurrencyViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path("docs/", schema_view),
	path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('username_filter/', UsernameFilterView.as_view(), name='username_filter'),
	path('email_filter/', EmailFilterView.as_view(), name='email_filter'),
	path('userid_filter/', UserIdFilterView.as_view(), name='userid_filter'),
	path('userid_keyword_filter/', UserIdKeywordFilterView.as_view(), name='userid_keyword_filter'),
	path('userid_data_keyword_filter/', UserIdDataKeywordFilterView.as_view(), name='userid_data_keyword_filter'),
	path('currency_filter/', CurrencyFilterView.as_view(), name='currency_filter'),
	path('currencyid_filter/', CurrencyIdFilterView.as_view(), name='currencyid_filter'),
	path('currency_keyword_filter/', CurrencyKeywordFilterView.as_view(), name='currency_keyword_filter'),
	path('vendor_roles_field/', VendorRolesApi.as_view(), name='vendor_roles_field'),
	path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.jwt')),
]
