from django.urls import path
from . import views
from hostel.admin import admin_site

urlpatterns = [
    # path('staff-login/', views.staff_login_view, name='staff_login'),
    path('rit_admin', admin_site.urls),
    path('student-login/', views.student_login_view, name='student_login'),
    path('male-hostel-booking/<str:admissionNo>', views.male_hostel_booking_view, name='male_hostel_booking'),
    path('female-hostel-booking/<str:admissionNo>', views.female_hostel_booking_view, name='female_hostel_booking'),
    path('booking-success/', views.booking_success_view, name='booking_success'),
    path('logout/', views.logout_view, name='logout'),
    path('male-current-bookings/', views.male_current_bookings_view, name='male_current_bookings'),
    path('female-current-bookings/', views.female_current_bookings_view, name='female_current_bookings'),
    path('booking-form/', views.booking_form, name='booking_form'),
    path('male-booking-success/', views.male_booking_success_view, name='male_booking_success'),
    path('female-booking-success/', views.female_booking_success_view, name='female_booking_success'),
    path('signup/', views.signup, name='signup'),
    path('faculty-login/', views.faculty_login, name='faculty_login'),  # Ensure this is correct
    path('gm-view/', views.gm_view, name='gm_view'),
    path('gm-approved-view/', views.gm_approved_view, name='gm_approved_view'),
    path('accept-booking/<int:booking_id>/', views.accept_booking, name='accept_booking'),  # Keep only one of these
    path('girlswarden-view/', views.girlswarden_view, name='girlswarden_view'),
    path('boyswarden-view/', views.boyswarden_view, name='boyswarden_view'),
    path('booking-success-view/', views.booking_success_view, name='booking_success_view'),
    path('gm/pending-bookings/', views.gm_pending_bookings_view, name='gm_pending_bookings_view'),
    path('authorize-girls-hostel/', views.authorize_girls_hostel, name='authorize_girls_hostel'),
    path('girls_approve_booking/<int:booking_id>/', views.girls_approve_booking, name='girls_approve_booking'),

    path('approve-booking/<int:booking_id>/',views.approve_booking, name='approve_booking'),
    path('approve-booking/<int:booking_id>/', views.approve_booking, name='approve_booking'),
  
    path('show-male-booking-details/<int:booking_id>/', views.show_male_booking_details, name='show_male_booking_details'),
    path('show-female-booking-details/<int:booking_id>/', views.show_female_booking_details, name='show_female_booking_details'),
    
    # by sheshan
   path('fees_detils/<str:admissionNo_year>/<str:gender>', views.fees_detils, name='fees_detils'),
   path('generate_pdf', views.generate_pdf, name='generate_pdf'),
    
]
