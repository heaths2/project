from rest_framework import serializers
from .models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'created_at', 'modified_at', 'url', 'email', 'username', 'mobile_number', 'date_of_birth', 'gender', 'date_joined', 'last_login']
