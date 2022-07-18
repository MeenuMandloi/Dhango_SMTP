from django.shortcuts import render
from SMTPproject.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.conf import settings

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome'
        message = 'Hope you are enjoying your work'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient])
        return render(request, 'success.html', {'recepient': recepient})

    return render(request, 'index.html', {'form': sub})

