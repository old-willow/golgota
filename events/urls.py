from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'events.views.eventspage', name='index'),
    url(r'(?P<date>\d{4}/\d{2})/$', 'events.views.eventspage', name='date'),
    url(r'(?P<id>\d{1,4})/$', 'events.views.detail_event', name='detail'),
)
