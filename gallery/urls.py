from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'gallery.views.gallery_home_page', name='index'),
    #url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})$', 'gallery.views.gallery_page', name='gallery'),
    url(r'(?P<gallery_id>\d{1,4})/$', 'gallery.views.gallery_page', name='gallery'),
)
