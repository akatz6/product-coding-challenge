from uuid import uuid4

# from django.db import models

# MAX_FORM_NAME_LENGTH = 128


# class Form(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     name = models.CharField(max_length=MAX_FORM_NAME_LENGTH)
#     number_of_steps = models.PositiveIntegerField()
    
#     STATE_CHOICES = [
#         ('new', 'New'),
#         ('draft', 'Draft'),
#         ('current', 'Current'),
#         ('past', 'Past'),
#     ]
#     state = models.CharField(
#         max_length=10,
#         choices=STATE_CHOICES,
#         default='new',
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.name
    
# class Field(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     option = models.CharField(max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Step(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     form = models.ForeignKey(Form, related_name='steps', on_delete=models.CASCADE)
#     name = models.CharField(max_length=MAX_FORM_NAME_LENGTH)
#     order = models.PositiveIntegerField()


from django.db import models
import uuid

MAX_FORM_NAME_LENGTH = 100  # Adjust this as needed




    
# class Form(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=MAX_FORM_NAME_LENGTH)
#     number_of_steps = models.PositiveIntegerField()
#     STATE_CHOICES = [
#         ('new', 'New'),
#         ('draft', 'Draft'),
#         ('current', 'Current'),
#         ('past', 'Past'),
#     ]
#     state = models.CharField(max_length=10, choices=STATE_CHOICES, default='new')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Step(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     form = models.ForeignKey(Form, related_name='steps', on_delete=models.CASCADE)
#     name = models.CharField(max_length=MAX_FORM_NAME_LENGTH)
#     order = models.PositiveIntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
       
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
        ('new', 'New'),
        ('draft', 'Draft'),
        ('current', 'Current'),
        ('past', 'Past'),
    ]
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='new')

    def __str__(self):
        return self.name

class Step(models.Model):
    form = models.ForeignKey(Form, related_name='steps', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.form.name} - Step {self.order}: {self.description}"