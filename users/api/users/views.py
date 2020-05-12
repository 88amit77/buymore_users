import json
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department
from .serializers import (
    UserSerializer,
    GroupSerializer,
    ContentTypeSerializer,
    PermissionSerializer,
    DepartmentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contenttypes to be viewed or edited.
    """
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsernameFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = User.objects.all().order_by('username')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'username' in request.data:
            qs = qs.filter(username__contains=request.data['username'])
        usernames = [{user.username: user.username} for user in qs]
        return Response(usernames)


class EmailFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = User.objects.all().order_by('email')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'email' in request.data:
            qs = qs.filter(email__contains=request.data['email'])
        email = [{user.email: user.email} for user in qs]
        return Response(email)


class UserIdFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = User.objects.all().order_by('id')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'user_id' in request.data:
            user_ids = request.data['user_id'].split(',')
            qs = qs.filter(id__in=user_ids)
        if 'username' in request.data:
            user_names = request.data['username'].split(',')
            qs = qs.filter(username__in=user_names)
        if 'email' in request.data:
            emails = request.data['email'].split(',')
            qs = qs.filter(email__in=emails)

        users = [{user.id: user.id} for user in qs]
        return Response(users)


class UserIdKeywordFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = User.objects.all().order_by('id')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'keyword' in request.data:
            qs = qs.filter(email__contains=request.data['keyword']) | qs.filter(username__contains=request.data['keyword']) | qs.filter(id__contains=request.data['keyword'])
        users = [{user.id: user.id} for user in qs]
        return Response(users)


class UserIdDataKeywordFilterView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        qs = User.objects.all().order_by('id')
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'keyword' in request.data:
            qs = qs.filter(username__contains=request.data['keyword']) | qs.filter(id__contains=request.data['keyword'])
        users = [{user.id: user.id} for user in qs]
        return Response(users)


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class VendorRolesApi(APIView):
    def get(self, request):
        vendor_department = Department.objects.get(pk=2)
        qs = vendor_department.groups.all()
        data = {}
        for group in qs:
            group_id = group.id
            name = group.name
            data[group_id] = name
        return Response(data)


class MarketingInchargeFieldApi(APIView):
    def get(self, request):
        users = User.objects.all()
        data = {}
        for user in users:
            user_id = user.id
            if user.first_name is not '' and user.first_name is not None:
                name = user.first_name
                if user.last_name is not None and user.last_name is not '':
                    name = name + ' ' + user.last_name
            else:
                name = user.username
            data[user_id] = name
        return Response(data)


class BrandAnalystFieldApi(APIView):
    def get(self, request):
        users = User.objects.all()
        data = {}
        for user in users:
            user_id = user.id
            if user.first_name is not '' and user.first_name is not None:
                name = user.first_name
                if user.last_name is not None and user.last_name is not '':
                    name = name + ' ' + user.last_name
            else:
                name = user.username
            data[user_id] = name
        return Response(data)


class CheckUsernameView(APIView):
    def get(self, request):
        user = User.objects.filter(username=request.data['username'])
        if len(user) > 0:
            return Response({"status": True})
        else:
            return Response({"status": False})


class CheckEmailView(APIView):
    def get(self, request):
        user = User.objects.filter(email=request.data['email'])
        if len(user) > 0:
            return Response({"status": True})
        else:
            return Response({"status": False})
