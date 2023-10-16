from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User


class MetaModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class UserType(MetaModel):
    type = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'UserTypes'


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    birth_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    type = models.ForeignKey(UserType, on_delete=models.RESTRICT, null=True, blank=True)

    class Meta:
        db_table= 'UserProfiles'

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Subject(MetaModel):
    subject_name = models.CharField(max_length=512, null=False, blank=False)


    class Meta:
        db_table = 'Subjects'

    def __str__(self):
        return self.subject_name


class Teacher(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)
    credits = models.IntegerField(default=0, null=True, blank=True)
    students = models.ManyToManyField("Student", null=True, blank=True)

    class Meta:
        db_table = 'Teachers'

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"



class Student(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)
    credits = models.IntegerField(default=0, null=True, blank=True)
    teachers = models.ManyToManyField(Teacher, null=True, blank=True)

    class Meta:
        db_table = 'Students'

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"


class StudentTeacherLesson(MetaModel):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    student_full_name = models.CharField(max_length=64, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)
    teacher_full_name = models.CharField(max_length=64, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.RESTRICT)
    record_url = models.URLField(null=True, blank=True)
    lesson_date = models.DateField(null=False, blank=False)
    lesson_material = models.URLField(null=True, blank=True)
    # The length in minutes
    length = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Lessons'

    def __str__(self):
        return f"{self.student} {self.teacher} {self.lesson_date}"

