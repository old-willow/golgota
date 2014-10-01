from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'medias.views.mediaspage', name='index'),
    url(r'archive/$', 'medias.views.medias_archive', name='archive-list'),
)
