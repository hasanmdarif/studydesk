from django.contrib import admin
from .models import Post
from .models import ContactUs
from import_export.admin import ExportActionMixin
class ContactAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_at')
    list_filter = ('created_at',)


admin.site.register(ContactUs, ContactAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
