from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'contact.views.contactpage', name='index'),
    url(r'message-sent/$', 'contact.views.message_sent', name='message-sent'),

    url(r'DEBUG/$', 'contact.views.DEBUG_info', name='DEBUG'),  # Only for debuging!
)
