from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inbox/', views.inbox, name='inbox'),

    # Send Message
    path('send-message/', views.send_message, name='send-message'),
    # Delete Message
    path('delete-message/<str:mail_id>/',
         views.delete_message, name='delete-message'),
    # View Message
    path('read-message/<str:mail_id>/', views.read_message, name='read-message'),
    # Mark Message
    path('mark-message/', views.mark_message, name='mark-message'),
    # Mark to auto log out
    path('autologout/', views.AutoLogoutUser, name='autologout'),
]
