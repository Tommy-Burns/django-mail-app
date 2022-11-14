from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'name', 'email', 'subject', 'message', 'file')
    list_display = ['name', 'email', 'subject', 'created', 'condition']
    search_fields = ['name', 'email', 'subject']
    List_filter = ['status']
    list_per_page = 10
