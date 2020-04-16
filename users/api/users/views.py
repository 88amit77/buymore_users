import json
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, ContentTypeSerializer, PermissionSerializer


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
        if 'keyword' in request.data:
            qs = qs.filter(email__contains=request.data['keyword']) | qs.filter(username__contains=request.data['keyword']) | qs.filter(id__contains=request.data['keyword'])
        if 'id' in request.data:
            ids = request.data['id'].split(',')
            qs = qs.filter(id__in=ids)
        if 'user_id' in request.data:
            qs = qs.filter(id__contains=request.data['user_id'])
        if 'username' in request.data:
            qs = qs.filter(username__contains=request.data['username'])
        if 'email' in request.data:
            qs = qs.filter(email__contains=request.data['email'])

        users = [{user.id: user.id} for user in qs]
        return Response(users)

