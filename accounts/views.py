from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer, CustomUserDetailsSerializer, UserListSerializer


class UserRegister(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileUpdate(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomUserDetailsSerializer

    def patch(self, request, *args, **kwargs):
        model = CustomUser.objects.get(id=request.user.id)
        serializer = CustomUserDetailsSerializer(model, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User Details Updated Successfully. ",
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()  # query result set
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)
