# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Active(models.Model):
    id = models.BigAutoField(primary_key=True)
    activeid = models.IntegerField(db_column='ActiveId', blank=True, null=True)  # Field name made lowercase.
    personid = models.IntegerField(db_column='PersonId', blank=True, null=True)  # Field name made lowercase.
    pairid = models.IntegerField(db_column='PairId', blank=True, null=True)  # Field name made lowercase.
    dat = models.DateTimeField(db_column='Dat', blank=True, null=True)  # Field name made lowercase.
    grade = models.FloatField(db_column='Grade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Groupa(models.Model):
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    nam = models.CharField(db_column='Nam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    course = models.IntegerField(db_column='Course', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'groupa'


class Pair(models.Model):
    pairid = models.BigAutoField(db_column='PairId', primary_key=True)  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='TeacherId', blank=True, null=True)  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectId', blank=True, null=True)  # Field name made lowercase.
    typesubjectid = models.IntegerField(db_column='TypeSubjectId', blank=True, null=True)  # Field name made lowercase.
    nam = models.CharField(db_column='Nam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dat = models.DateTimeField(db_column='Dat', blank=True, null=True)  # Field name made lowercase.
    num = models.IntegerField(db_column='Num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pair'


class Student(models.Model):
    personid = models.BigAutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=10)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    chatid = models.BigIntegerField(db_column='ChatID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=320, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Subject(models.Model):
    subjectid = models.BigAutoField(db_column='SubjectID', primary_key=True)  # Field name made lowercase.
    nam = models.CharField(db_column='Nam', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subject'


class Teacher(models.Model):
    teacherid = models.BigAutoField(db_column='TeacherID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='JobTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    academicdegree = models.CharField(db_column='AcademicDegree', max_length=50, blank=True, null=True)  # Field name made lowercase.
    рcademictitle = models.CharField(db_column='└cademicTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chatid = models.IntegerField(db_column='ChatID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'


class Typeactive(models.Model):
    id = models.BigAutoField(primary_key=True)
    nam = models.CharField(db_column='Nam', max_length=50, blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typeactive'


class Typesubject(models.Model):
    subjectid = models.BigAutoField(db_column='SubjectID', primary_key=True)  # Field name made lowercase.
    nam = models.CharField(db_column='Nam', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typesubject'
