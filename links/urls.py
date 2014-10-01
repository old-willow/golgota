from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'links.views.linkspage', name='index'),
)
