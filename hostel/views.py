from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from .forms import RoomBookingForm, FacultySignupForm, FacultyLoginForm,userform
from .models import Booking, Room, Student,Academic_Details,Faculty,boys_hostel_master,User as HostelUser,girls_hostel_master,fees,PersonalForm
from django.db import connections
from django.contrib import messages
from django.contrib.auth.models import User
import hashlib
from django.contrib.auth.hashers import check_password
import datetime as dt
from urllib.parse import quote,unquote
import os
from django.core.mail import EmailMessage

def encrypt_password(password: str) -> str:
    # Hash a password
    return hashlib.sha256(password.encode()).hexdigest()


# Example usage
password = "my_secure_password"
encrypted_password = encrypt_password(password)
print(encrypted_password)

def student_login_view(request):
    gq=girls_hostel_master.objects.filter(quota="GQ")
    
    if request.method == 'POST':
        aadhaar_number = request.POST.get('aadhaar_number')

        # Query to get personal data from application_personal_details
        query = '''
            SELECT Name, Gender, Mode, Aadhaar_Number, Department,admissionNo
            FROM admissionform.application_personal_details
            WHERE Aadhaar_Number = %s
        '''

        with connections['admissionform'].cursor() as cursor:
            cursor.execute(query, [aadhaar_number])
            personal_data = cursor.fetchone()

        if personal_data:
            # Unpack the result into named variables
            name, gender, mode, aadhaar_number, department,admissionNo = personal_data

            # Store details in session
            request.session['student_name'] = name
            request.session['department'] = department
            request.session['aadhaar_number'] = aadhaar_number
            request.session['admissionNo'] = admissionNo
            admissionNo = request.session['admissionNo']

            batch_1 = admissionNo.split('-')[0]
            batch = batch_1 + '-' + str(int(batch_1) + 4)[-2:]
            
            currect_year = (dt.datetime.now().year-int(batch_1))+1
            new_admissionNo= admissionNo+'/'+str(currect_year)
            encoded_admissionNo = new_admissionNo.replace('/','*')

            request.session['new_admissionNo'] = new_admissionNo


            mode = mode.strip().lower()
            gender = gender.strip().capitalize()

            fees_data = fees.objects.filter(admissionNo_year=new_admissionNo)
            booked_data = Booking.objects.filter(admissionNo=new_admissionNo)
            print(new_admissionNo,"************")
            if mode == 'hostel':
                if gender == 'Female':
                    if not fees_data :
                        return redirect('fees_detils',admissionNo_year=encoded_admissionNo,gender='Female')
                    elif fees_data and not booked_data:
                        return redirect('female_hostel_booking',admissionNo=encoded_admissionNo)
                    else:
                        return redirect("female_current_bookings")
                else:
                    if not fees_data :
                        return redirect('fees_detils',admissionNo_year=encoded_admissionNo,gender='Male')
                    elif fees_data and not booked_data:
                        return redirect('male_hostel_booking',admissionNo=encoded_admissionNo)
                    else:
                        return redirect("male_current_bookings")
            else:
                return render(request, 'error.html', {
                    'message': 'Sorry, you are not a Hosteller,',
                    'personal_data': {
                        'Name': name,
                        'Gender': gender,
                        'Mode': mode,
                        'Aadhaar_Number': aadhaar_number
                    }
                })
        else:
            return render(request, 'error.html', {'message': 'Invalid Aadhaar Number.'})

    return render(request, 'login.html')



def male_hostel_booking_view(request,admissionNo):
    admissionNo_year=admissionNo.replace('*','/')
    admissionNo_session = request.session['admissionNo']
    batch_1 = admissionNo_session.split('-')[0]
    batch = batch_1 + '-' + str(int(batch_1) + 4)[-2:]
    print(admissionNo_year)
    # Check if the student already has a booking
    existing_booking = Booking.objects.filter(admissionNo=admissionNo_year, gender='Male').first()
    print(admissionNo_year,existing_booking)
    if existing_booking != None:
        print(admissionNo_year)
        # If a booking exists, redirect to the booking details view
        return redirect('male_current_bookings')

    data = Academic_Details.objects.using('admissionform').filter(admissionNo=admissionNo_session).values_list('ScholarShip', "admissionNo").first()

    if request.method == 'POST':
        number_of_occupants = int(request.POST.get('number_of_occupants', 0))
        room_id = request.POST.get('room_number')
        room = boys_hostel_master.objects.get(room_no=room_id)
        
        # Collect occupant details
        occupant_details = []
        for i in range(1, number_of_occupants + 1):
            occupant_name = request.POST.get(f'occupant_{i}_name', '')
            occupant_roll_number = request.POST.get(f'occupant_{i}_roll_number', '')
            if occupant_name and occupant_roll_number:
                occupant_details.append({'name': occupant_name, 'roll_number': occupant_roll_number})

        # Create a new booking
        booking = Booking(
            student_name=request.session.get('student_name'),
            department=request.session.get('department'),
            batch=batch,
            room_number=room.room_no,
            occupants=number_of_occupants,
            gender='Male',
            admissionNo=admissionNo_year
        )
        booking.save()

        # Mark the room as occupied
        room.is_occupied = True
        room.save()

        return render(request,'male_booking_success.html',{"admissionNo":admissionNo})

    # Retrieve available rooms and other necessary data
    number_of_occupants = int(request.GET.get('number_of_occupants', 1))  # Default to 1 if not provided
    occupants_range = range(1, number_of_occupants + 1)
    available_rooms = Room.objects.filter(is_occupied=False, gender_specific='male')

    # Retrieve room data based on conditions
    # if data[0] == 'GOVT_SCHOOL':
    #     query = '''
    #         SELECT room_no FROM hostel.hostel_boys_hostel_master WHERE block LIKE 'Common Room-%'
    #     '''
    # else:
    query = '''
        SELECT
            hbhm.room_no
        FROM
            hostel_boys_hostel_master hbhm
        LEFT JOIN
            hostel_booking hb
        ON
            hbhm.room_no = hb.room_number 
        GROUP BY
            hbhm.room_no, hbhm. no_of_occupants 	
        HAVING
            COALESCE(COUNT(hb.id), 0) < hbhm. no_of_occupants 	;
    '''
    
    with connections['default'].cursor() as cursor:
        cursor.execute(query)
        room_data = cursor.fetchall()
    print(room_data)
    rooms = [row[0] for row in room_data]

    # Retrieve student details for auto-fill
    student_name = request.session.get('student_name')
    department = request.session.get('department')

    context = {
        'number_of_occupants': number_of_occupants,
        'occupants_range': occupants_range,
        'available_rooms': rooms,
        'student_name': student_name,
        'department': department,
        "admissionNo":admissionNo_year
    }

    return render(request, 'male_hostel_booking.html', context)




def female_hostel_booking_view(request,admissionNo):
    admissionNo_year=admissionNo.replace('*','/')
    admissionNo_session = request.session['admissionNo']
    batch_1 = admissionNo_session.split('-')[0]
    batch = batch_1 + '-' + str(int(batch_1) + 4)[-2:]
    
    
    # Check if the student already has a booking
    existing_booking = Booking.objects.filter(admissionNo=admissionNo_year, gender='Female').first()
    
    if existing_booking:
        # If a booking exists, redirect to the booking details view
        return redirect('female-current-bookings', booking_id=existing_booking.id)

    data = Academic_Details.objects.using('admissionform').filter(admissionNo=admissionNo_session).values_list('ScholarShip', "admissionNo").first()

    if request.method == 'POST':
        number_of_occupants = int(request.POST.get('number_of_occupants', 0))
        room_id = request.POST.get('room_number')
        room = girls_hostel_master.objects.get(room_no=room_id)

        # Collect occupant details
        occupant_details = []
        for i in range(1, number_of_occupants + 1):
            occupant_name = request.POST.get(f'occupant_{i}_name', '')
            occupant_roll_number = request.POST.get(f'occupant_{i}_roll_number', '')
            if occupant_name and occupant_roll_number:
                occupant_details.append({'name': occupant_name, 'roll_number': occupant_roll_number})

        # Create a new booking
        booking = Booking(
            student_name=request.session.get('student_name'),
            department=request.session.get('department'),
            batch=batch,
            room_number=room.room_no,
            occupants=number_of_occupants,
            gender='Female',
            admissionNo=admissionNo_year
        )
        print(booking)
        booking.save()

        # Mark the room as occupied
        # room.is_occupied = True
        # room.save()
        return render(request,'female_booking_success.html',{"admissionNo":admissionNo})


    number_of_occupants = int(request.GET.get('number_of_occupants', 1))  # Default to 1 if not provided
    occupants_range = range(1, number_of_occupants + 1)
    available_rooms = Room.objects.filter(is_occupied=False, gender_specific='female')

    if data[0] == 'GOVT_SCHOOL':
        query = '''
            SELECT
            hbhm.room_no
        FROM
            hostel_girls_hostel_master hbhm
        LEFT JOIN
            hostel_booking hb
        ON
            hbhm.room_no = hb.room_number
        WHERE
            hbhm.room_no IN (
                SELECT
                    room_no
                FROM
                    hostel_girls_hostel_master
                WHERE
                    quota = 'GQ'
            )
        GROUP BY
            hbhm.room_no, hbhm.no_of_occupants
        HAVING
            COALESCE(COUNT(hb.id), 0) < hbhm.no_of_occupants;
        '''
    else:
        query = '''
            SELECT
            hbhm.room_no
        FROM
            hostel_girls_hostel_master hbhm
        LEFT JOIN
            hostel_booking hb
        ON
            hbhm.room_no = hb.room_number
        WHERE
            hbhm.room_no IN (
                SELECT
                    room_no
                FROM
                    hostel_girls_hostel_master
                WHERE
                    quota != 'GQ'
            )
        GROUP BY
            hbhm.room_no, hbhm.no_of_occupants
        HAVING
            COALESCE(COUNT(hb.id), 0) < hbhm.no_of_occupants;
        '''
    # for future 
    # query = '''
    #         SELECT room_no FROM hostel.hostel_girls_hostel_master
    #     '''
    with connections['default'].cursor() as cursor:
        cursor.execute(query)
        room_data = cursor.fetchall()
    
    rooms = [row[0] for row in room_data]

    # Retrieve student details for auto-fill
    student_name = request.session.get('student_name')
    department = request.session.get('department')

    context = {
        'number_of_occupants': number_of_occupants,
        'occupants_range': occupants_range,
        'available_rooms': rooms,
        'student_name': student_name,
        'department': department,
        "admissionNo":admissionNo
    }

    return render(request, 'female_hostel_booking.html', context)




def booking_success_view(request):
    return render(request, 'booking_success.html')

def logout_view(request):
    
    print('logout function called')
    auth_logout(request)
    messages.success(request,'You were logged out')
    request.session.flush()  # Flush all session data
    return redirect("student_login")


def male_current_bookings_view(request):
    new_admissionNo=request.session['new_admissionNo'] 
    room_no= Booking.objects.filter(admissionNo=new_admissionNo).values('room_number').first()
    bookings = Booking.objects.filter(room_number=room_no['room_number'],admissionNo__endswith=new_admissionNo.split('/')[-1]).order_by('-date_booked')
    print(bookings)
    return render(request, 'male_current_bookings.html', {'bookings': bookings,})


def female_current_bookings_view(request):
    new_admissionNo=request.session['new_admissionNo'] 

    room_no= Booking.objects.filter(admissionNo=new_admissionNo).values('room_number').first()
    print(new_admissionNo.split('/')[-1],room_no['room_number'])
    bookings = Booking.objects.filter(room_number=room_no['room_number'],admissionNo__endswith=new_admissionNo.split('/')[-1]).order_by('-date_booked')
    print(bookings)
    return render(request, 'female_current_bookings.html', {'bookings': bookings})


def booking_form(request):
    available_rooms = Room.objects.filter(is_occupied=False)
    return render(request, 'room_booking.html', {'available_rooms': available_rooms})

def male_booking_success_view(request):
    return render(request, 'male_booking_success.html')
def female_booking_success_view(request):
    return render(request, 'female_booking_success.html')



def gm_view(request):
    if request.session.get('user_auth'):
        if request.method == 'POST':
            selected_bookings = request.POST.getlist('bookings')
            if selected_bookings:
                # Approve the selected bookings by the GM
                Booking.objects.filter(id__in=selected_bookings, warden_approved=True).update(status='Accepted', gm_approved=True)
                messages.success(request, 'Selected bookings approved by GM!')
                return redirect('gm_view')

        # Show only bookings pending GM approval that are already approved by the warden
        boys_pending_bookings = Booking.objects.filter(gender='Male', warden_approved=True, gm_approved=False)
        girls_pending_bookings = Booking.objects.filter(gender='Female', warden_approved=True, gm_approved=False)

        context = {
            'boys_pending_bookings': boys_pending_bookings,
            'girls_pending_bookings': girls_pending_bookings,
        }

        return render(request, 'gm_view.html', context)
    else:
        return redirect('student_login')


def accept_booking(request, booking_id):
    if request.session.get('user_auth'):
        booking = get_object_or_404(Booking, id=booking_id)
        if booking.warden_approved:
            booking.status = 'Accepted'  # Update the status of the booking
            booking.gm_approved = True  # GM approval flag
            booking.save()
        else:
            messages.error(request, 'Booking must be approved by the warden first.')
        return redirect('gm_view')
    else:
        return redirect('student_login')

def gm_approved_view(request):
    if request.session.get('user_auth'):
        boys_pending_gm_approval = Booking.objects.filter(warden_approved=True, gm_approved=False, gender='Male')
        girls_pending_gm_approval = Booking.objects.filter(warden_approved=True, gm_approved=False, gender='Female')

        boys_approved_bookings = Booking.objects.filter(warden_approved=True, gm_approved=True, gender='Male')
        girls_approved_bookings = Booking.objects.filter(warden_approved=True, gm_approved=True, gender='Female')

        if request.method == 'POST':
            selected_bookings = request.POST.getlist('bookings')
            for booking_id in selected_bookings:
                booking = Booking.objects.get(id=booking_id)
                if booking.warden_approved:
                    booking.gm_approved = True
                    booking.status = 'Accepted'
                    booking.save()
                else:
                    messages.error(request, f'Booking ID {booking_id} must be approved by the warden first.')
            messages.success(request, 'Selected bookings approved by GM!')
            return redirect('gm_approved')

        return render(request, 'GM_approved_view.html', {
            'boys_pending_gm_approval': boys_pending_gm_approval,
            'girls_pending_gm_approval': girls_pending_gm_approval,
            'boys_approved_bookings': boys_approved_bookings,
            'girls_approved_bookings': girls_approved_bookings,
        })
    else:
        return redirect('student_login')

def gm_pending_bookings_view(request):
    if request.session.get('user_auth'):
        boys_pending_bookings = Booking.objects.filter(status='Pending', warden_approved=False, gender='Male')
        girls_pending_bookings = Booking.objects.filter(status='Pending', warden_approved=False, gender='Female')

        context = {
            'boys_pending_bookings': boys_pending_bookings,
            'girls_pending_bookings': girls_pending_bookings,
        }
        return render(request, 'gm_view.html', context)
    else:
        return redirect('student_login')

def authorize_girls_hostel(request):
    if request.session.get('user_auth'):
        girls_pending_bookings = Booking.objects.filter(warden_approved=True, gm_approved=False, gender='Female')
        return render(request, 'girls_gm_view.html', {'girls_pending_bookings': girls_pending_bookings})
    else:
        return redirect('student_login')

def signup(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            department=request.GET.get('Department')
            password = form.cleaned_data['Password']
            confirm_password = form.cleaned_data['confirm_Password']

            if password == confirm_password:
                encrypted_password = encrypt_password(password)
                
                    

                    # Save the encrypted password to your user model
                user = form.save(commit=False)  # Don't save the form yet
                user.Password = encrypted_password
                user.confirm_Password = encrypted_password

                user.save()

                # Redirect to a success page or login page
                return redirect('student_login')
            
            else:
                # Passwords don't match, return an error
                form.add_error('confirm_password', 'Passwords do not match')
                return render(request, "faculty_signup", {'form': form})
        # else:
        #     return render(request, "error.html", {'form': form})
    else:
        form = userform()

    return render(request, "faculty_signup.html", {'form': form,"working":"working"})


def faculty_login(request):
    print("View called")  # Debugging line

    if request.method == 'POST':
        print("POST method detected")  # Debugging line

        staff_id = request.POST.get('staff_id')
        password = request.POST.get('password')
        print(f"Received staff_id: {staff_id}, password: {password}")  # Debugging line

        try:
            user = HostelUser.objects.get(staff_id=staff_id)
            print(f"User found: {user}")  # Debugging line
        except HostelUser.DoesNotExist:
            print("User not found")  # Debugging line
            return render(request, 'login.html', {'error': 'Invalid staff ID'})

        if  user.Password == encrypt_password(password):
            print(encrypt_password(password))
            print(f"User {staff_id} authenticated successfully")  # Debugging line
            # auth_login(request, user)

            if user.role == 'GM':
                request.session['user_auth'] = True
                return redirect('gm_view')
            elif user.role == 'Boys Warden':
                request.session['user_auth'] = True
                return redirect('boyswarden_view')
            elif user.role == 'Girls Warden':
                request.session['user_auth'] = True
                return redirect('girlswarden_view')
            else:
                request.session['user_auth'] = True
                return redirect('default_view')
        else:
            print("Invalid password")  # Debugging line
            return render(request, 'login.html', {'error': 'Invalid password'})
    else:
        print("Not a POST request")  # Debugging line

    return render(request, 'login.html')


def show_male_booking_details(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, gender='Male')
    return render(request, 'male_booking_details.html', {'booking': booking})

def show_female_booking_details(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, gender='Female')
    return render(request, 'female_booking_details.html', {'booking': booking})



# by sheshan
def save_uploaded_pdfs(file_dict):
    profile_images_directory = os.path.join('media')
    os.makedirs(profile_images_directory, exist_ok=True)

    file_paths = {}

    for field_name, file_obj in file_dict.items():
        base_file_name = f'{field_name}_{file_obj.name}'
        file_path = os.path.join(profile_images_directory, base_file_name)

        # Check if the file already exists, if yes, append a number
        counter = 1
        while os.path.exists(file_path):
            new_file_name = f'{field_name}_{counter}_{file_obj.name}'
            file_path = os.path.join(profile_images_directory, new_file_name)
            counter += 1

        with open(file_path, 'wb') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)

        file_paths[field_name] = file_path
    return file_paths

def fees_detils(request, admissionNo_year,gender):
    admissionNo_year_or = admissionNo_year.replace('*', '/')
    if request.method == 'POST':
        fees_amount = request.POST.get('fees_amount')
        proof = request.FILES.get('proof')  
        file_paths = save_uploaded_pdfs(request.FILES) if proof else {}
        path = file_paths.get('proof')
        data = fees(admissionNo_year=admissionNo_year_or,amount=fees_amount,proof=path)
        data.save()
        if gender == "Female":
            return redirect('female_hostel_booking',admissionNo=admissionNo_year)
        elif gender == "Male":
            return redirect('male_hostel_booking',admissionNo=admissionNo_year)
    return render(request, 'fees.html')




def boyswarden_view(request):
    if request.session.get('user_auth'):
        if request.method == 'POST':
            aadhaar_number = request.POST.get('aadhaar_number')

            # Query to fetch admission number
            query = '''
                SELECT admissionNo
                FROM admissionform.application_personal_details
                WHERE Aadhaar_Number = %s
            '''
            with connections['admissionform'].cursor() as cursor:
                cursor.execute(query, [aadhaar_number])
                personal_data = cursor.fetchone()

            if personal_data:
                admission_no = personal_data[0]
                # Update the warden approval in the Booking table
                booking = Booking.objects.filter(admissionNo=admission_no, gender='male', warden_approved=False).first()
                if booking:
                    booking.warden_approved = True
                    booking.status = 'Pending GM Approval'  # Change status to indicate GM approval needed
                    booking.save()

            return redirect('boyswarden_view')  # Redirect back to the warden view to see updated list

        # Fetch pending bookings that have not been approved by the warden
        pending_bookings = Booking.objects.filter(gender='male', warden_approved=False)
        return render(request, 'boys_warden_pending_bookings.html', {'bookings': pending_bookings})
    else:
        return render(request, 'login.html')






def girlswarden_view(request):
    if request.method == 'POST':
        aadhaar_number = request.POST.get('aadhaar_number')

        # Query to fetch admission number
        query = '''
            SELECT admissionNo
            FROM admissionform.application_personal_details
            WHERE Aadhaar_Number = %s
        '''
        with connections['admissionform'].cursor() as cursor:
            cursor.execute(query, [aadhaar_number])
            personal_data = cursor.fetchone()

        # Update the warden approval in the Booking table
        if personal_data:
            admission_no = personal_data[0]
            booking = Booking.objects.filter(admissionNo=admission_no, gender='female').first()
            if booking:
                booking.warden_approved = True
                booking.status = 'Accepted'
                booking.save()

        return redirect('girlswarden_view')  # Redirect to Girls GM view for final approval

    # Fetch pending bookings that have not been approved by the warden
    pending_bookings = Booking.objects.filter(gender='female', warden_approved=False)
    return render(request, 'girls_warden_pending_bookings.html', {'bookings': pending_bookings})



def girls_approve_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
        booking.warden_approved = True
        booking.status = 'Pending GM Approval'
        booking.save()
        return redirect('girlswarden_view')
    except Booking.DoesNotExist:
        return render(request, 'error.html', {'message': 'Booking not found.'})




def approve_booking(request, booking_id):
    # Fetch the booking instance
    booking = get_object_or_404(Booking, id=booking_id)

    # Check if the booking has already been warden-approved
    if not booking.warden_approved:
        booking.warden_approved = True
        booking.status = 'Pending GM Approval'  # Status should reflect GM approval is needed
        booking.save()

    # Redirect to GM approval view
    return redirect('boyswarden_view')

import requests
from django.core.mail import EmailMessage
def generate_pdf(request):
    role = request.GET.get('role')

    if role == 'staff':
        if request.method == "POST":
            aad_no = request.POST.get("aadhar_number")
            
            query = '''
                SELECT admissionNo
                FROM admissionform.application_personal_details
                WHERE Aadhaar_Number = %s
            '''
            with connections['admissionform'].cursor() as cursor:
                cursor.execute(query, [aad_no])
                personal_data = cursor.fetchone()
            
            if personal_data:
                admissionNo = personal_data[0]
                batch_1 = admissionNo.split('-')[0]
                currect_year = (dt.datetime.now().year - int(batch_1)) + 1
                new_admissionNo = admissionNo + '/' + str(currect_year)

                # Fetch the PDF generated by the PHP script
                pdf_url = f'http://localhost:8080/fpdf/hostel_form.php?admissionNo={admissionNo}&new_admissionNo={new_admissionNo}'
                
                # Uncomment and adjust the email sending part if needed
                # response = requests.get(pdf_url)
                # if response.status_code == 200:
                #     email = EmailMessage(
                #         subject='Your Hostel Form PDF',
                #         body='Please find the attached hostel form PDF.',
                #         from_email='riteapproval@gmail.com',
                #         to=['pavotigris9218@gmail.com'],  # replace with the recipient's email
                #     )
                #     email.attach('hostel_form.pdf', response.content, 'application/pdf')
                #     email.send()

                return redirect(pdf_url)  # Redirect the user to the PDF URL
            else:
                # Handle case where no personal data is found
                return HttpResponse("Aadhaar number not found.", status=404)

    elif role == "student":
        aadhaar_number = request.session.get('aadhaar_number')
       
        query = '''
                SELECT Self_Email_ID, Gender 
                FROM admissionform.application_personal_details
                WHERE Aadhaar_Number = %s
            '''
        with connections['admissionform'].cursor() as cursor:
            cursor.execute(query, [aadhaar_number])
            personal_data = cursor.fetchone()
        
        if personal_data:
            self_mail, gender = personal_data
            admissionNo = request.session.get('admissionNo')
            new_admissionNo = request.session.get('new_admissionNo') 
            pdf_url = f'http://localhost:8080/fpdf/hostel_form.php?admissionNo={admissionNo}&new_admissionNo={new_admissionNo}'
            
            subject_create = 'Your Subject Here'
            message_create = 'This is a test email sent from Django.'
            # email = self_mail
            email="riteapproval@gmail.com"
            
            # Fetch the PDF generated by the PHP script
            response = requests.get(pdf_url)
            print(response)

            if response.status_code == 200:
                # Create an email message object with the subject and message
                email_message = EmailMessage(
                    subject=subject_create,
                    body=message_create,
                    from_email="riteapproval@gmail.com",
                    to=[email],
                )

                # Attach the PDF content to the email
                email_message.attach('hostel_form.pdf', response.content, 'application/pdf')

                # Send the email
                email_message.send(fail_silently=False)
                
                return redirect(pdf_url)
            else:
                return HttpResponse("Failed to retrieve the PDF.", status=500)
        else:
            # Handle case where no personal data is found
            return HttpResponse("Aadhaar number not found.", status=404)
    else:
        return HttpResponse("Invalid role specified.", status=400)
