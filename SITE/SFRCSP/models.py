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
    grade = models.IntegerField(db_column='Grade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'active'


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


class Pairactiv(models.Model):
    id = models.PositiveBigIntegerField()
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pairactiv'


class Student(models.Model):
    personid = models.BigAutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=10)  # Field name made lowercase.
    groupid = models.IntegerField(db_column='GroupID', blank=True, null=True)  # Field name made lowercase.
    chatid = models.BigIntegerField(db_column='ChatID', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=320, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.

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
    academictitle = models.CharField(db_column='AcademicTitle', max_length=50, blank=True, null=True)  # Field name made lowercase.
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
