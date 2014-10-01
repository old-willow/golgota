from django.conf.urls import patterns, include, url

# I found this article to be so far the best explaination for translating:
#http://stackoverflow.com/questions/18392405/issue-trying-to-change-language-from-django-template
# This works for me now. But it seems to me that this is not how the
# documentation explains, or I don't understed. Maybe i18n_patterns is used
# only if I want a langugae prefixes in urls. (Aug 8, 2014.)
#from django.conf.urls.i18n import i18n_patterns

# This is only during development, see:
# https://docs.djangoproject.com/en/1.6/howto/static-files/deployment/
# for Deploying static files in real productin environment.
from golgota import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

#import home


urlpatterns = patterns('',
#    #url(r'^$', include('home.urls', namespace='home')),
#    # Home page has different urls among home page and I can't figure out how
#    # to put this in home.urls conf file Apr 29, 2014.
#    #url(r'^staff/(?P<slug>\w{2,15})/$', 'home.views.staff_detail', name='staff-detail'),
#
#    #url(r'^events/', include('events.urls', namespace='events')),
#    #url(r'^gallery/', include('gallery.urls', namespace='gallery')),
#    #url(r'^medias/', include('medias.urls', namespace='medias')),
#    #url(r'^contact/', include('contact.urls', namespace='contact')),
#    #url(r'^links/', include('links.urls', namespace='links')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
#    #url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^staff/(?P<slug>\w{2,15})/$', 'home.views.staff_detail', name='staff-detail'),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^medias/', include('medias.urls', namespace='medias')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^links/', include('links.urls', namespace='links')),
    url(r'^admin/', include(admin.site.urls)),
)
