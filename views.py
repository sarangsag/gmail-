from django.shortcuts import render

# Create your views here.
# def index(request):
#     return render(request,"index.html")

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SubscribeForm

# def
def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            # name =form.cleaned_data.get('name')
            # contact =form.cleaned_data.get('contact')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            recipient ="sarang5271@gmail.com"

            send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recipient],fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('subscribe')
    return render(request, 'index.html', {'form': form})