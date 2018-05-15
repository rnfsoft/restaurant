from django import forms

from .models import RestaurantLocation
from .validators import validate_category


class RestaurantLocationCreateForm(forms.ModelForm):
    #category         = forms.CharField(required=False, validators=[validate_category])
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
        ]
    
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name