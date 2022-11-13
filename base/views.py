from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
@cache_control(no_cache=True, must_validate=True, no_store=True)
def inbox(request):
    return render(request, 'inbox.html')