from django.contrib import admin
from .models import ContactFormSubmission
from .models import Student


admin.site.register(ContactFormSubmission)



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email')
