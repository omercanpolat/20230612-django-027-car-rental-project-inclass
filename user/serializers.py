from rest_framework import serializers

# -------------------------------
# UserSerializer
# -------------------------------
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        required = False,
        write_only = True,
    )

    class Meta:
        model = User
        exclude = []
        
    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password
            password = attrs['password']
            validate_password(password)
            attrs.update({'password': make_password(password)})
        return super().validate(attrs)