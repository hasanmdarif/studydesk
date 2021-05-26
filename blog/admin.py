from django.contrib import admin

# Register your models here.
from .models import ContactUs
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_at')
    list_filter = ('created_at',)


admin.site.register(ContactUs, ContactAdmin)