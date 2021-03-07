from django import forms
from .models import GuestResponse

class GuestResponseForm(forms.ModelForm):

    class Meta:
        model = GuestResponse
        fields = [
            'guest_name',
            'able_to_attend',
            'adults',
            'children',
            'comments'
            ]
        widgets = {
            'able_to_attend': forms.RadioSelect,
            'adults': forms.Textarea(attrs={'rows':3, 'cols':15}),
            'children': forms.Textarea(attrs={'rows':3, 'cols':15}),
            'comments': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }
        labels = {
            "guest_name": "What is your first and last name?",
            'able_to_attend': "Are you able to attend the wedding?",
            'adults': "Please list full names of the adults in your group:",
            'children': "Please list full names of the children in your group:",
            'comments': "Comments/Questions:",

        }