from django import forms
from .models import Student, Room, Faculty,User
from django.contrib.auth.forms import AuthenticationForm

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'year', 'department']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number', 'year', 'department']

class RoomSelectionForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number']

class StudentLoginForm(forms.Form):
    roll_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Roll Number'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class RoomBookingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        number_of_occupants = kwargs.pop('number_of_occupants', 1)
        super().__init__(*args, **kwargs)
        
        self.fields['name'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
        self.fields['department'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}))
        self.fields['room_number'] = forms.ModelChoiceField(queryset=Room.objects.filter(is_occupied=False), 
                                                            widget=forms.Select(attrs={'class': 'form-control'}), 
                                                            empty_label="Select a Room")
        
        for i in range(2, number_of_occupants + 1):
            self.fields[f'occupant_{i}_name'] = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': f'Occupant {i} Name'}))
            self.fields[f'occupant_{i}_roll_number'] = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': f'Occupant {i} Roll Number'}))






class FacultySignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Faculty
        fields = ['name', 'staff_id', 'department', 'email', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

class FacultyLoginForm(forms.Form):
    class Meta:
        model = User
        fields = [
           'staff_id',  'Password' ]

class userform(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'Name', 'user_name', 'staff_id', 'Department', 'email','Department_code',
            'role', 'Password', 'confirm_Password'
 ]
        exclude=['Department_code']
