from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

from base.forms import CustomerForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
@cache_control(no_cache=True, must_validate=True, no_store=True)
def inbox(request):
    return render(request, 'inbox.html')


def send_message(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully")
        return HttpResponseRedirect('/')
    else:
        form = CustomerForm()
    return render(request, 'home.html', {
        'form': form,
    })
