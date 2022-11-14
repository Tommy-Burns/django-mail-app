from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inbox/', views.inbox, name='inbox'),
    
    # Send Message
    path('send-message/', views.send_message, name='send-message'),
]