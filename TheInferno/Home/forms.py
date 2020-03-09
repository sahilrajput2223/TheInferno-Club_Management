from django import forms
from .models import Profile, Bookclub,Contact,Feedback

class DateInput(forms.DateInput):
    input_type = 'Date'
    format = '%m/%d/%Y'
    input_format = '%m/%d/%Y'

class Profile_form(forms.ModelForm):
    class Meta:
        model =Profile
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': DateInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(Profile_form, self).__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['gender'].label = ''
        self.fields['address'].label = ''
        self.fields['DOB'].label = ''
        self.fields['contact'].label = ''
        self.fields['pincode'].label = ''


class edit_Profile_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','readonly':True}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'DOB': DateInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(edit_Profile_form, self).__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['email'].label = ''
        self.fields['gender'].label = ''
        self.fields['address'].label = ''
        self.fields['DOB'].label = ''
        self.fields['contact'].label = ''
        self.fields['pincode'].label = ''


class Bookclub_from(forms.ModelForm):
    class Meta:
        model = Bookclub
        fields = ['email','Date']

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'Date': DateInput(attrs={'placeholder': 'Date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(Bookclub_from, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['Date'].label = 'Date'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'Message': forms.TextInput(attrs={'class': 'form-control'}),
        }



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'feedback': forms.TextInput(attrs={'class': 'form-control'}),
        }