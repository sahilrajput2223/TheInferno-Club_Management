from django import forms
from .models import Amenities

class Amenities_form(forms.ModelForm):
    class Meta:
        model = Amenities
        fields = '__all__'

