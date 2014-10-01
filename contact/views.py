from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.conf import settings
from django.core.mail import send_mail

from contact.forms import ContactForm
from contact.models import Contacts

from django.core.urlresolvers import reverse

from golgota import settings


def contactpage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            # Sending email.
            subject = form.cleaned_data['subject']
            email = [form.cleaned_data['email'], settings.EMAIL_HOST_USER, ]
            message = form.cleaned_data['message']

            send_mail(subject, message, settings.EMAIL_HOST_USER, email, fail_silently=False)

            url = reverse('contact:message-sent')
            return HttpResponseRedirect(url)
    else:
        form = ContactForm(
            initial={
                'name': u'Kolo\u017ei Robert',
                'email': u'kolozi@eunet.rs',
                'subject': u'[Django] Test from gmail to eunet.rs subject',
                'message': u'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas et nunc id felis condimentum ullamcorper nec a orci. Morbi placerat convallis pharetra. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin volutpat id massa et pulvinar. Etiam est ligula, imperdiet sed sollicitudin vitae, vehicula id nunc. Maecenas at sollicitudin nunc, at fringilla nisi. Duis egestas lorem tristique, suscipit nisi nec, commodo sem. Nulla ac eros nec leo tincidunt bibendum a eget felis. Nunc consectetur enim ligula, vel egestas quam rutrum in.',
                'web_site': u'http://www.robertkolozsi.org'
            }
        )

    context = {
        'form': form,
    }
    return render_to_response('contact/index.html',
                              context,
                              context_instance=RequestContext(request))


def message_sent(request):
    """
    This function is called once Contact form is submited sucessfully.
    """
    contacts = Contacts.objects.latest('date_submited')

    context = {
        'contact': contacts,
    }

    return render_to_response('contact/message_sent.html',
                              context,
                              context_instance=RequestContext(request))


def DEBUG_info(request):
    """
    DEBUG function anly for testing and checking data in database.
    """
    contacts = Contacts.objects.all()
    table_name = Contacts._meta.db_table

    context = {
        'contacts': contacts,
        'table_name': table_name,
    }

    return render_to_response('contact/DEBUG.html',
                              context,
                              context_instance=RequestContext(request))
