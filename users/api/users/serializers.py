from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from .models import Department, Import, Export


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'user_permissions', 'password']
        write_only_fields = ['password']
        ref_name = 'api_users'

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        user = User.objects.create_user(**validated_data)
        user.groups.set(groups)
        print(user)
        return user

class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Import
        fields = '__all__'


class ListImportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Import
        fields = ('import_id', 'user_id', 'imfile_name', 'imfile_type', 'imfile_size', 'imfile_isread'
                  , 'imfile_iscompleted', 'created_date', 'updated_date')


class ExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Export
        fields = '__all__'


class ListExportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Export
        fields = ('export_id', 'user_id', 'exfile_name', 'exfile_size', 'exfile_iscreated','exfile_isdownloaded','created_date', 'updated_date')
