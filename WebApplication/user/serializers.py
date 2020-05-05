from rest_framework import serializers
from .models import User


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'phone', 'date_of_birth', 'gender',
                  'date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff', 'is_superuser']


# 회원가입 시리얼라이저

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["email"], None, validated_data["password"]
        )
        return user


# 접속 유지중인지 확인할 시리얼라이저

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username")


# 로그인 시리얼라이저

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, kwargs):
        user = authenticate(**kwargs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")
