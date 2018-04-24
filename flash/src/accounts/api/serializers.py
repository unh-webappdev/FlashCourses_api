"""
FlashCourses REST API User Registration Serializer

File Path:     /flash/src/accounts/api/serializers.py

Modified By:   Patrick R. McElhiney
Date Modified: 4/20/2018
"""
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.six import text_type
from ..models import UserProfile
from rest_framework.serializers import (
        ModelSerializer,
        SerializerMethodField,
        EmailField,
        CharField,
        ValidationError
)

class RegistrationSerializer(ModelSerializer):
    email = EmailField(required=True, label="Email")
    email2 = EmailField(required=True, label="Retype Email")
    username = CharField(required=True, label="Username", validators=[UniqueValidator(queryset=User.objects.all())])
    password = CharField(required=True, label="Password", style={'input_type': 'password'}, write_only=True)
    password2 = CharField(required=True, label="Retype Password", style={'input_type': 'password'}, write_only=True)

    token = SerializerMethodField(source='get_token')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'email2', 'password', 'password2', 'token']
        #extra_kwargs required to add password-hash
        extra_kwargs = {
                         "password": {"write_only":True},
                         "password2": {"write_only":True}
                       }

    def validate_email(self, value):
        data =  self.get_initial()
        email1 = value
        email2 = data.get("email2")
        
        if email1!=email2:
            raise ValidationError("Emails must match.")
        
        #validating existing email
        user_qs = User.objects.filter(email=email1)
        if user_qs.exists():
            raise ValidationError("Email already exists.")
        
        return value

    def validate_email2(self, value):
        data =  self.get_initial()
        email1 = data.get("email")
        email2 = value

        if email1!=email2:
            raise ValidationError("Emails must match.")

        #validating existing email
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("Email already exists.")
        
        return value

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        data =  self.get_initial()
        password1 = data.get("password2")
        password2 = value
        
        if password1!=password2:
            raise ValidationError("Passwords must match.")
        
        return value

    def validate_password2(self, value):
        password_validation.validate_password(value, self.instance)
        data =  self.get_initial()
        password1 = data.get("password")
        password2 = value
        
        if password1!=password2:
            raise ValidationError("Passwords must match.")
        
        return value

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']

        user_obj = User(
                username=username,
                email = email
                )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


    def get_token(self, validated_data):
        attrs = {
            'username': self.initial_data['username'],
            'password': self.initial_data['password']
        }
        return ThisTokenObtainPairSerializer().validate(attrs)


class ThisTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        return token

    def validate(self, attrs):
        data = super(TokenObtainPairSerializer, self).validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = text_type(refresh)
        data['access'] = text_type(refresh.access_token)

        return data
