from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField(default=1)
    is_occupied = models.BooleanField(default=False)
    gender_specific = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])

    def __str__(self):
        return self.room_number

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    department = models.CharField(max_length=100)
    room = models.OneToOneField(Room, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_incharge = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    admissionNo = models.CharField(max_length=255,null=True)
    batch = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    occupants = models.IntegerField()
    date_booked = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')  # Add status field

    def __str__(self):
        return f"Booking by {self.student_name} for room {self.room_number}"

    def get_occupants(self):
        # Return occupant_details directly if it's already a list
        return self.occupant_details

class PersonalDetails(models.Model):
    
    admissionNo = models.CharField(max_length=20, primary_key=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    Mode = models.CharField(max_length=100)
    Aadhaar_Number = models.CharField(max_length=12)

    class Meta:
        db_table = 'application_personal_details'
        managed = False

class PersonalForm(models.Model):
    Name = models.CharField(max_length=100)
    admissionNo = models.CharField(max_length=20, primary_key=True)
    Gender = models.CharField(max_length=10)
    Aadhaar_Number = models.CharField(max_length=12)  # Adjusted length
    date = models.DateField(auto_now_add=True)
    Quota = models.CharField(max_length=50, blank=True, null=True)
    Department = models.CharField(max_length=50, blank=True, null=True)
    Father_name = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    Mobile_Number = models.CharField(max_length=15, blank=True, null=True)
    cutoffmark = models.CharField(max_length=50, blank=True, null=True)
    gm_conform = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'application_personalform'
        managed = False




class FacultyManager(BaseUserManager):
    def create_user(self, staff_id, name, email, department, role, password=None, **extra_fields):
        if not staff_id:
            raise ValueError('The Staff ID field must be set')
        user = self.model(staff_id=staff_id, name=name, email=email, department=department, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, staff_id, name, email, department, role, password=None, **extra_fields):
        user = self.create_user(staff_id, name, email, department, role, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user

class Faculty(AbstractBaseUser):
    staff_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=50)  # e.g., 'gm', 'principal', 'vice_principal', etc.
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = FacultyManager()

    USERNAME_FIELD = 'staff_id'
    REQUIRED_FIELDS = ['name', 'email', 'department', 'role']

    def __str__(self):
        return self.staff_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Academic_Details(models.Model):
    # personal = models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    admissionNo = models.CharField(max_length=20)
    Counselling_Application_No = models.CharField(max_length=100,blank=True,null=True)
    GQ_Admission_Number = models.CharField(max_length=100,blank=True,null=True)
    Counselling_General_Rank = models.CharField(max_length=100,blank=True,null=True)
    ScholarShip = models.CharField(max_length=100,blank=True,null=True)
    First_Graduate_certificate_No = models.CharField(max_length=100,blank=True,null=True)
    govper = models.CharField(max_length=100,blank=True,null=True)
    Occupation = models.CharField(max_length=50)
    Job_Details = models.CharField(max_length=100)
    Annual_Income = models.CharField(max_length=50)
    Name_of_Std_6th_10th = models.CharField(max_length=100,blank=True,null=True)
    Std_6th_10th_schooltype = models.CharField(max_length=50,blank=True,null=True)
    School_Name_of_Std_11th_12th = models.CharField(max_length=100,blank=True,null=True)
    Std_11th_12th_School_Type = models.CharField(max_length=50,blank=True,null=True)
    Name_of_the_Bank = models.CharField(max_length=100)
    Branch_Name_of_the_Bank = models.CharField(max_length=100)
    Branch_Code_No = models.CharField(max_length=20,blank=True,null=True)
    IFSC = models.CharField(max_length=20)
    MICR = models.CharField(max_length=20)
    Bank_Holder_Name = models.CharField(max_length=100)
    Account_No = models.CharField(max_length=20)
    How = models.CharField(max_length=100)
    dateadmission = models.DateField(auto_now_add=True)
    admission_Category = models.CharField(max_length=50,blank=True,null=True)
    academic_year = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
        db_table = 'application_academic_details'
        managed = False

class boys_hostel_master(models.Model):
    batch = models.IntegerField()
    year = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    room_no = models.CharField(max_length=50, unique=True)
    no_of_occupants = models.IntegerField()

    