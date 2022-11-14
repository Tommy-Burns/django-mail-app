import uuid
from django.db import models
from django.utils.html import format_html

# Create your models here.
class Customer(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Read', 'Read'),
    )
    # primary_key=True, default=uuid.uuid4, editable=False
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=30)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=2000)
    file = models.FileField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUS)
    
    # Control Read/Unread messagesin admin.py
    def condition(self):
        if self.status == 'Read':
            return format_html('<span style="color: green">{0}</span>', self.status)
        else:
            return format_html('<span style="color: red">{0}</span>', self.status)
        
    condition.allow_tags = True
    
    def __str__(self):
        return self.name
            