from uuid import uuid4

from django.db import models

MAX_FORM_NAME_LENGTH = 128


class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(max_length=MAX_FORM_NAME_LENGTH)
    
    STATE_CHOICES = [
        ('new', 'New'),
        ('draft', 'Draft'),
        ('current', 'Current'),
        ('past', 'Past'),
    ]
    state = models.CharField(
        max_length=10,
        choices=STATE_CHOICES,
        default='new',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Field(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    option = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

