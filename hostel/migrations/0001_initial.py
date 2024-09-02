# Generated by Django 4.2.14 on 2024-08-28 11:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionNo', models.CharField(max_length=20)),
                ('Counselling_Application_No', models.CharField(blank=True, max_length=100, null=True)),
                ('GQ_Admission_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('Counselling_General_Rank', models.CharField(blank=True, max_length=100, null=True)),
                ('ScholarShip', models.CharField(blank=True, max_length=100, null=True)),
                ('First_Graduate_certificate_No', models.CharField(blank=True, max_length=100, null=True)),
                ('govper', models.CharField(blank=True, max_length=100, null=True)),
                ('Occupation', models.CharField(max_length=50)),
                ('Job_Details', models.CharField(max_length=100)),
                ('Annual_Income', models.CharField(max_length=50)),
                ('Name_of_Std_6th_10th', models.CharField(blank=True, max_length=100, null=True)),
                ('Std_6th_10th_schooltype', models.CharField(blank=True, max_length=50, null=True)),
                ('School_Name_of_Std_11th_12th', models.CharField(blank=True, max_length=100, null=True)),
                ('Std_11th_12th_School_Type', models.CharField(blank=True, max_length=50, null=True)),
                ('Name_of_the_Bank', models.CharField(max_length=100)),
                ('Branch_Name_of_the_Bank', models.CharField(max_length=100)),
                ('Branch_Code_No', models.CharField(blank=True, max_length=20, null=True)),
                ('IFSC', models.CharField(max_length=20)),
                ('MICR', models.CharField(max_length=20)),
                ('Bank_Holder_Name', models.CharField(max_length=100)),
                ('Account_No', models.CharField(max_length=20)),
                ('How', models.CharField(max_length=100)),
                ('dateadmission', models.DateField(auto_now_add=True)),
                ('admission_Category', models.CharField(blank=True, max_length=50, null=True)),
                ('academic_year', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'application_academic_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalDetails',
            fields=[
                ('admissionNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
                ('Mode', models.CharField(max_length=100)),
                ('Aadhaar_Number', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'application_personal_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PersonalForm',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('admissionNo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Gender', models.CharField(max_length=10)),
                ('Aadhaar_Number', models.CharField(max_length=12)),
                ('date', models.DateField(auto_now_add=True)),
                ('Quota', models.CharField(blank=True, max_length=50, null=True)),
                ('Department', models.CharField(blank=True, max_length=50, null=True)),
                ('Father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('place', models.CharField(blank=True, max_length=50, null=True)),
                ('Mobile_Number', models.CharField(blank=True, max_length=15, null=True)),
                ('cutoffmark', models.CharField(blank=True, max_length=50, null=True)),
                ('gm_conform', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'application_personalform',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('occupants', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('date_booked', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='boys_hostel_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField()),
                ('year', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=50)),
                ('block', models.CharField(max_length=50)),
                ('room_no', models.CharField(max_length=50, unique=True)),
                ('no_of_occupants', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('staff_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='girls_hostel_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.IntegerField()),
                ('year', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=50)),
                ('block', models.CharField(max_length=50)),
                ('room_no', models.CharField(max_length=50, unique=True)),
                ('no_of_occupants', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('capacity', models.IntegerField(default=1)),
                ('is_occupied', models.BooleanField(default=False)),
                ('gender_specific', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20, unique=True)),
                ('year', models.IntegerField()),
                ('department', models.CharField(max_length=100)),
                ('room', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hostel.room')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
