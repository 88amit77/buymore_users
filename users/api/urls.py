from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_swagger.views import get_swagger_view

# TODO: add here your API URLs

schema_view = get_swagger_view(title='Micromerce API')


urlpatterns = [
	path("users/docs/", schema_view),
	path('users/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('users/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]
