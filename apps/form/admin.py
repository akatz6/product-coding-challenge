from django.contrib import admin
from apps.form.models import Form, Field, Step, Section

admin.site.register(Form)
admin.site.register(Field)
admin.site.register(Step)
admin.site.register(Section)