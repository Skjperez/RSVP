from django.forms import ModelForm
from .models import GuestResponse

class GuestResponseForm(ModelForm):
    class Meta:
        model = GuestResponse
        fields = [
            'guest_name',
            'able_to_attend',
            'adults',
            'children',
            'comments'
            ]