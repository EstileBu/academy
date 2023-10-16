from django.shortcuts import render
from django.db import IntegrityError, transaction

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *

# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         with transaction.atomic():
#             serializer = UserSerializer(data=request.data)
#             if serializer.is_valid()
#

@api_view(['GET', 'PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    try:
        user_profile = UserProfile.objects.get(user= request.user)
    except:
        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        if user_profile.type.type == 'student':
            serializer = StudentSerializer(Student.objects.get(profile=user_profile))
            return Response(serializer.data)
        elif user_profile.type.type == 'teacher':
            serializer = TeacherSerializer(Teacher.objects.get(profile=user_profile))
            return Response(serializer.data)

    if request.method == 'PATCH':
        user = User.objects.get(id = request.user.id)
        user.first_name = request.data['first_name']
        #
        # The same for all the other field
        #
        profile = UserProfile.objects.get(user=request.user)
        #
        # The same for all the other field
        #

        user.save()
        profile.save()
        return Response(status.HTTP_200_OK)

