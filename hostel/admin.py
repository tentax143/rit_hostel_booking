
from django.contrib import admin
#from .models import Room, Student, Staff, Booking, Faculty
import django.apps
class hostel_admin(admin.AdminSite):
    site_header='hostel_booking'
admin_site=hostel_admin(name='hostel_admin')

models=django.apps.apps.get_models()
for model in models:
    try:
        admin_site.register(model)
    except:
        print("model not found")

# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('room_number', 'capacity', 'is_occupied', 'gender_specific')  # Added gender_specific
#     search_fields = ('room_number',)
#     list_filter = ('is_occupied', 'capacity', 'gender_specific')  # Added gender_specific filter

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'roll_number', 'year', 'department', 'room')
#     search_fields = ('name', 'roll_number', 'department')
#     list_filter = ('year', 'department')

# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('user', 'is_incharge')
#     search_fields = ('user__username',)

# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('student_name', 'department', 'room_number', 'occupants', 'date_booked', 'status')
#     search_fields = ('student_name', 'room_number')
#     list_filter = ('date_booked', 'status')
#     actions = ['delete_selected']

#     def delete_selected(self, request, queryset):
#         queryset.delete()
#         self.message_user(request, "Selected bookings have been deleted successfully.")
#     delete_selected.short_description = "Delete selected bookings"

# class MaleRoomAdmin(admin.ModelAdmin):
#     list_display = ('room_number', 'capacity', 'gender_specific')
#     list_filter = ('gender_specific',)
#     search_fields = ('room_number',)

# class FemaleRoomAdmin(admin.ModelAdmin):
#     list_display = ('room_number', 'capacity', 'gender_specific')
#     list_filter = ('gender_specific',)
#     search_fields = ('room_number',)

# admin.site.register(Room, RoomAdmin)
# admin.site.register(Student, StudentAdmin)
# admin.site.register(Staff, StaffAdmin)
# admin.site.register(Booking, BookingAdmin)
# admin.site.register(Faculty)
