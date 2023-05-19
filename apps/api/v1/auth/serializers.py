from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from django.utils.translation import gettext_lazy as _

from apps.api.v1.base.validate import validate_email
from apps.users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            validate_email,
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    username = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise ValidationError(_("password must be equal to password2"))

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
