from django import forms
from contact.models import Contacts

from django.utils import timezone


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        exclude = ('date_submited', )  # Don't show this field on form.

    def __unicode__(self):
        return '%s --> %s' % (self.name, self.email)

    def save(self):
        """
        Store message data to database.
        """
        saved_data = Contacts.objects.create(
            name = self.cleaned_data['name'],
            email = self.cleaned_data['email'],
            subject = self.cleaned_data['subject'],
            message = self.cleaned_data['message'],
            date_submited = timezone.now(),
            web_site = self.cleaned_data['web_site']
        )

        return saved_data
