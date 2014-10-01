from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'home.views.homepage', name='index'),
    #url(r'^staff/(?P<last_name>\w{5,15})/$', 'home.views.staff_detail', name='staff-detail'),
)
