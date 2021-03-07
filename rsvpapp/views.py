from django.shortcuts import render, redirect

from .models import GuestResponse
from .forms import GuestResponseForm


def index(request):
    context = {'form': GuestResponseForm}
    return render(request, 'rsvpapp/index.html', context)

def confirmation(request):
    if request.method == 'POST':
        form = GuestResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://jonathanlovesshonnetta.com/rsvp/confirmed/')
            #return render(request, 'rsvpapp/confirm.html')
    else:
        context = {
            'form': GuestResponseForm,
            'error_message': 'Fill out all fields'}
        return render(request, 'rsvpapp/index.html', context)