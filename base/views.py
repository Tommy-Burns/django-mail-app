from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from base.forms import CustomerForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from base.models import Customer
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
@cache_control(no_cache=True, must_validate=True, no_store=True)
def inbox(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_customer_list = Customer.objects.filter(
            Q(name__icontains=q) | Q(email=q) |
            Q(subject__icontains=q) | Q(message__icontains=q) |
            Q(status__icontains=q)
        ).order_by('-created')
    else:
        all_customer_list = Customer.objects.all().order_by('-created')

    paginator = Paginator(all_customer_list, 6)
    page = request.GET.get('page')
    all__messages = paginator.get_page(page)

    # All Messages
    total = Customer.objects.all().count()
    # Read Messages
    read = Customer.objects.filter(status='Read')
    # Unread Messages
    unread = Customer.objects.filter(status='Pending')
    # Today's Messages
    day = datetime.now().date()
    today = Customer.objects.filter(created__gt=day)

    return render(request, 'inbox.html', {
        'mails': all__messages,
        'total': total,
        'read': read,
        'pending': unread,
        'today': today,
    })


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


@login_required(login_url='login')
@cache_control(no_cache=True, must_validate=True, no_store=True)
def delete_message(request, mail_id):
    mail = Customer.objects.get(id=mail_id)
    if mail is not None:
        mail.delete()
        messages.success(request, "Message successfully deleted.")
    else:
        messages.error(request, "An error occured and message wasn't deleted.")
    return HttpResponseRedirect('/inbox')


@login_required(login_url='login')
@cache_control(no_cache=True, must_validate=True, no_store=True)
def read_message(request, mail_id):
    mail = Customer.objects.get(id=mail_id)

    if mail != None:
        return render(request, 'mail.html', {
            'mail': mail,
        })
