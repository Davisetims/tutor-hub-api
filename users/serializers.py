from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_superuser'] = user.is_superuser
        token['username'] = user.username
        token['email'] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        """Get user info"""
        user_data = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            'is_tutor': self.user.is_tutor,
            "is_superuser": self.user.is_superuser,
            'profile_picture': self.user.profile_picture.url if self.user.profile_picture else None,
            'bio':self.user.bio if self.user.bio else None,
            'phone_number': self.user.phone_number if self.user.phone_number else None,
        }

        data.update({"user": user_data})

        return data

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'is_tutor','first_name', 'last_name', 'phone_number',
                  'bio', 'profile_picture','email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)
        return data

    def create(self, validated_data):
        password = validated_data.get('password')
        if password:
            validated_data['password'] = make_password(password)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            """Hash the new password"""
            instance.set_password(password)

        return super().update(instance, validated_data)

