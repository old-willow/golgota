from django.contrib import admin

from contact.models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'message', 'web_site', 'date_submited']

admin.site.register(Contacts, ContactsAdmin)
