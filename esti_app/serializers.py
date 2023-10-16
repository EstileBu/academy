from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'first_name',
            'last_name'
        )
        extra_kwargs = {'password':{'write_only':True}}
        depth = 0

    def save(self):
        user = User(email=self.validated_data['email'],
                    username=self.validated_data['email'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name']
                    )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        depth = 1

    def save(self, type, **kwargs):
        newProfile = UserProfile(
            birth_date=self.validated_data['birth_date'],
            phone_number=self.validated_data['phone_number'],
            address=self.validated_data['address'],
            user=self.instance,
            type=type
        )
        newProfile.save()
        return newProfile



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTeacherLesson
        fields = "__all__"
        depth = 1


class TeacherSerializer(serializers.ModelSerializer):
    class Metea:
        model = Teacher
        fields = ['id', 'credits', 'profile', 'subjects']
        depth = 2

    def save(self, **kwargs):
        newTeacher = Teacher(profile=self.instance)
        newTeacher.save()
        return newTeacher


class StudentSerializer(serializers.ModelSerializer):
    class Metea:
        model = Student
        fields = ['id', 'credits', 'profile', 'subjects']
        depth = 2

    def save(self, **kwargs):
        newStudent = Student(profile=self.instance)
        newStudent.save()
        return newStudent




# GET - to receive data, get request doesnt have parameters/body.
# POST - to post data, has parametsr/body, exmaples: register, login. it  holds data (like password)
# PATCH - update the object. it can hold just a part of the properties
# PUT - update the object. it must hold all the properties.
# DELETE - has bo body, used to delete an object.



