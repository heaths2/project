from rest_framework import serializers
from .models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'date_of_birth', 'gender', 'date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser']
