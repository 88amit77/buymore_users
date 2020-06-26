import json
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Department, Import, Export
from .serializers import (
    UserSerializer,
    GroupSerializer,
    ContentTypeSerializer,
    PermissionSerializer,
    DepartmentSerializer,
    ImportSerializer,
    ListImportSerializer,
    ExportSerializer,
    ListExportSerializer,
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


class UserNameDataKeywordFilterView(APIView):
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
            qs = qs.filter(username__contains=request.data['keyword'])
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

#for import and export api
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters

DEFAULT_PAGE = 1
class CustomImportPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                    'user_id',
                    'imfile_name',
                ],
                'header': {

                    'user_id':'User Name',
                    'imfile_name':'File Name',
                    'imfile_type':'File Type',
                    'imfile_size':'File Size',
                    'imfile_isread': 'Is Read',
                    'imfile_iscompleted': 'Is Completed',
                    'created_date':'Created At',
                    'updated_date':'Updated At',

                   },
                'sortable': [
                    'user_id',
                    'imfile_name',
                ],
                'searchable': [
                    'user_id',
                    'imfile_name',
                    'imfile_type',
                    'imfile_size',
                    'imfile_isread',
                    'imfile_iscompleted',
                    'created_date',
                    'updated_date',

                ],

            },
            'results': data
        })

class CustomExportPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 20
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'UI_data': {
                'sticky_headers': [
                    'user_id',
                    'exfile_name',
                ],
                'header': {

                    'user_id':'User Name',
                    'exfile_name':'File Name',
                    'exfile_type':'File Type',
                    'exfile_size':'File Size',
                    'exfile_iscreated': 'Is Read',
                    'exfile_iscompleted': 'Is Completed',
                    'created_date':'Created At',
                    'updated_date':'Updated At',

                   },
                'sortable': [
                    'user_id',
                    'exfile_name',
                ],
                'searchable': [
                    'user_id',
                    'exfile_name',
                    'exfile_type',
                    'exfile_size',
                    'exfile_iscreated',
                    'exfile_iscompleted',
                    'created_date',
                    'updated_date',

                ],

            },
            'results': data
        })

class ImportViewSet(viewsets.ModelViewSet):

    queryset = Import.objects.all()
    serializer_class = ImportSerializer
    # permission_classes = [permissions.IsAuthenticated]

class ListImportViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = Import.objects.all()
        serializer = ListImportSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomImportPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListImportSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomImportPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)

class SearchImportViewSet(viewsets.ModelViewSet):
    search_fields = [

        'user_id',
        'imfile_name',
        'imfile_type',
        'imfile_size',
        'imfile_isread',
        'imfile_iscompleted',
        'created_date',
        'updated_date',

    ]
    ordering_fields = ['user_id', 'imfile_name',]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Import.objects.all()
    serializer_class = ListImportSerializer
    pagination_class = CustomImportPagination


class ExportViewSet(viewsets.ModelViewSet):

    queryset = Export.objects.all()
    serializer_class = ExportSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ListExportViewSet(viewsets.ViewSet):
    # pagination_class = CustomPagination
    def create(self, request):
        queryset = Export.objects.all()
        serializer = ListExportSerializer(queryset, many=True)
        if len(queryset) > 0:
            paginator = CustomExportPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            serializer = ListExportSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            paginator = CustomExportPagination()
            result_page = paginator.paginate_queryset(queryset, request)
            return paginator.get_paginated_response(result_page)

class SearchExportViewSet(viewsets.ModelViewSet):
    search_fields = [
        'user_id',
        'exfile_name',
        'exfile_size',
        'exfile_type',
        'exfile_iscreated',
        'exfile_iscompleted',
        'created_date',
        'updated_date',
                    ]
    ordering_fields = ['user_id', 'exfile_name',]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    queryset = Export.objects.all()
    serializer_class = ListExportSerializer
    pagination_class = CustomExportPagination