from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'email', 'info', 'number')
    list_display_links = ('id', 'name',)
    list_editable = ('info',)
    search_fields = ('name', 'gender')
    list_filter = ('gender',)
    list_per_page = 10

admin.site.register(Contact, ContactAdmin)
