from uuid import uuid4
from django.db import models

MAX_FORM_NAME_LENGTH = 100  # Adjust this as needed



       
class Field(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    option = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100)
    number_of_steps = models.PositiveIntegerField()
    STATE_CHOICES = [
        ('draft', 'Draft'),
        ('current', 'Current'),
        ('past', 'Past'),
    ]
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    form = models.ForeignKey(Form, related_name='steps', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.form.name} - Step {self.order}: {self.description}"
    
class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    step = models.ForeignKey(Step, related_name='sections', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    text = models.CharField(max_length=50)
    field = models.ForeignKey(Field, related_name='sections', on_delete=models.CASCADE)
    style = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.step.form.name} - Step {self.step.order}: Section {self.order}: {self.text}"