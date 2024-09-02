from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db import models


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
    Self_Email_ID = models.EmailField()

    class Meta:
        db_table = 'application_personalform'
        managed = False

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


class PersonalDetails(models.Model):
    
    admissionNo = models.CharField(max_length=20, primary_key=True)
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    Mode = models.CharField(max_length=100)
    Aadhaar_Number = models.CharField(max_length=12)

    class Meta:
        db_table = 'application_personal_details'
        managed = False

class boys_hostel_master(models.Model):
    batch = models.CharField(max_length=100)
    year = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    room_no = models.CharField(max_length=50, unique=True)
    no_of_occupants = models.IntegerField()



class girls_hostel_master(models.Model):
    batch = models.IntegerField()
    year = models.CharField(max_length=50)
    floor = models.CharField(max_length=50)
    block = models.CharField(max_length=50)
    room_no = models.CharField(max_length=50, unique=True)
    no_of_occupants = models.IntegerField()
    quota = models.CharField(max_length=100, default='General') 
    


class FacultyManager(BaseUserManager):
    def create_user(self, staff_id, name, department, email, role, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(
            staff_id=staff_id,
            name=name,
            department=department,
            email=email,
            role=role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Faculty(AbstractBaseUser):
    staff_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'staff_id'
    REQUIRED_FIELDS = ['name', 'department', 'email', 'role']

    objects = FacultyManager()

    def __str__(self):
        return self.name

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

# class Booking(models.Model):
#     batch = models.CharField(max_length=100)
#     date_booked = models.DateTimeField(auto_now_add=True)
#     department = models.CharField(max_length=100)
#     gender = models.CharField(max_length=10)
#     gm_approved = models.BooleanField(default=False)
#     id = models.AutoField(primary_key=True)
#     occupants = models.IntegerField()
#     room_number = models.CharField(max_length=100)
#     status = models.CharField(max_length=100)
#     student_name = models.CharField(max_length=100)
#     warden_approved = models.BooleanField(default=False)
#     admissionNo = models.CharField(max_length=100,null=True)


#     # New fields for approval statuses
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Accepted', 'Accepted'),
#     ]
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
#     warden_approved = models.BooleanField(default=False)
#     gm_approved = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.student_name} - {self.room_number}"

#     def get_occupants(self):
#         # Return occupant_details directly if it's already a list
#         return self.occupant_details

class Booking(models.Model):
    batch = models.CharField(max_length=100)
    date_booked = models.DateTimeField(auto_now_add=True)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    occupants = models.IntegerField()
    room_number = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    admissionNo = models.CharField(max_length=100, null=True)

    # Approval statuses and choices
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    warden_approved = models.BooleanField(default=False)
    gm_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_name} - {self.room_number}"

    def get_occupants(self):
        # Return occupant_details directly if it's already a list
        return self.occupant_details


class User(models.Model):
    Name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    staff_id = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Department_code=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    confirm_Password = models.CharField(max_length=100)

# by sheshan

class fees(models.Model):
    admissionNo_year = models.CharField(max_length=100)
    amount = models.IntegerField()
    proof =  models.CharField(max_length=100)