# Generated by Django 5.0.1 on 2024-03-10 10:58

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('activeid', models.IntegerField(blank=True, db_column='ActiveId', null=True)),
                ('personid', models.IntegerField(blank=True, db_column='PersonId', null=True)),
                ('pairid', models.IntegerField(blank=True, db_column='PairId', null=True)),
                ('dat', models.DateTimeField(blank=True, db_column='Dat', null=True)),
                ('grade', models.IntegerField(blank=True, db_column='Grade', null=True)),
            ],
            options={
                'db_table': 'active',
            },
        ),
        migrations.CreateModel(
            name='Groupa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupid', models.IntegerField(blank=True, db_column='GroupID', null=True)),
                ('nam', models.CharField(blank=True, db_column='Nam', max_length=50, null=True)),
                ('course', models.IntegerField(blank=True, db_column='Course', null=True)),
            ],
            options={
                'db_table': 'groupa',
            },
        ),
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('pairid', models.BigAutoField(db_column='PairId', primary_key=True, serialize=False)),
                ('teacherid', models.IntegerField(blank=True, db_column='TeacherId', null=True)),
                ('subjectid', models.IntegerField(blank=True, db_column='SubjectId', null=True)),
                ('typesubjectid', models.IntegerField(blank=True, db_column='TypeSubjectId', null=True)),
                ('nam', models.CharField(blank=True, db_column='Nam', max_length=50, null=True)),
                ('dat', models.DateTimeField(blank=True, db_column='Dat', null=True)),
                ('num', models.IntegerField(blank=True, db_column='Num', null=True)),
            ],
            options={
                'db_table': 'pair',
            },
        ),
        migrations.CreateModel(
            name='Pairactiv',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pairactiv',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('personid', models.BigAutoField(db_column='PersonID', primary_key=True, serialize=False)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=50, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=50, null=True)),
                ('middlename', models.CharField(blank=True, db_column='MiddleName', max_length=50, null=True)),
                ('nickname', models.CharField(db_column='NickName', max_length=10)),
                ('groupid', models.IntegerField(blank=True, db_column='GroupID', null=True)),
                ('chatid', models.BigIntegerField(blank=True, db_column='ChatID', null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=320, null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectid', models.BigAutoField(db_column='SubjectID', primary_key=True, serialize=False)),
                ('nam', models.CharField(blank=True, db_column='Nam', max_length=50, null=True)),
            ],
            options={
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacherid', models.BigAutoField(db_column='TeacherID', primary_key=True, serialize=False)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=50, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=50, null=True)),
                ('middlename', models.CharField(blank=True, db_column='MiddleName', max_length=50, null=True)),
                ('jobtitle', models.CharField(blank=True, db_column='JobTitle', max_length=50, null=True)),
                ('academicdegree', models.CharField(blank=True, db_column='AcademicDegree', max_length=50, null=True)),
                ('academictitle', models.CharField(blank=True, db_column='AcademicTitle', max_length=50, null=True)),
                ('chatid', models.IntegerField(blank=True, db_column='ChatID', null=True)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Typeactive',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nam', models.CharField(blank=True, db_column='Nam', max_length=50, null=True)),
                ('method', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'typeactive',
            },
        ),
        migrations.CreateModel(
            name='Typesubject',
            fields=[
                ('subjectid', models.BigAutoField(db_column='SubjectID', primary_key=True, serialize=False)),
                ('nam', models.CharField(blank=True, db_column='Nam', max_length=50, null=True)),
            ],
            options={
                'db_table': 'typesubject',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ElectronicJournal.student')),
                ('teacher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ElectronicJournal.teacher')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
