
from rest_framework import serializers

from accounts.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model =CustomUser
        fields= ['first_name' ,'last_name' ,'email',  'password' ,]

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model =CustomUser
        fields= ['first_name' ,'last_name' ,'designation',  'team' ,'image']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['first_name' ,'last_name' ,'email','designation',  'team' ,'image']