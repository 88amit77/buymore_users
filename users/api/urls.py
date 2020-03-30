from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view
from .users import views
# TODO: add here your API URLs

schema_view = get_swagger_view(title='Micromerce API')
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'contenttypes', views.ContentTypeViewSet)
router.register(r'permissions', views.PermissionViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path("docs/", schema_view),
	path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('auth/', include('djoser.urls')),
	path('auth/', include('djoser.urls.jwt')),
]
