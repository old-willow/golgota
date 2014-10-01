from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from datetime import datetime

from events.models import Event


class Gallery(models.Model):
    name_sr = models.CharField(_('gallery name on serbian'), max_length=100)
    name_hu = models.CharField(_('gallery name on hungarian'), max_length=100)
    name_en = models.CharField(_('gallery name on english'), max_length=100)
    date_created = models.DateTimeField(_('date when gallery created'),
                                        default=timezone.now)
    short_description_sr = models.CharField(_('short description on serbian'),
                                            max_length=256,
                                            help_text=_('shortly describe gallery'))
    short_description_hu = models.CharField(_('short description on hungarian'),
                                            max_length=256,
                                            help_text=_('shortly describe gallery'))
    short_description_en = models.CharField(_('short description on english'),
                                            max_length=256,
                                            help_text=_('shortly describe gallery'))
    description_sr = models.TextField(_('gallery\'s longer description on serbian'),
                                      max_length=2000,
                                      blank=True, null=True, default=None,
                                      help_text=_('describe gallery'))
    description_hu = models.TextField(_('gallery\'s longer description on hungarian'),
                                      max_length=2000,
                                      blank=True, null=True, default=None,
                                      help_text=_('describe gallery'))
    description_en = models.TextField(_('gallery\'s longer description on english'),
                                      max_length=2000,
                                      blank=True, null=True, default=None,
                                      help_text=_('describe gallery'))
    event = models.ForeignKey(Event, help_text=_('choose event'),
                              blank=True, null=True, default=None)
    slug = models.SlugField()
    is_publishable = models.BooleanField(_('is gallery publishable?'),
                                         default=False)

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return self.name_sr
        elif translation.get_language() == 'hu':
            return self.name_hu
        elif translation.get_language() == 'en':
            return self.name_en


class Image(models.Model):
    title_sr = models.CharField(_('image title on serbian'), max_length=50)
    title_hu = models.CharField(_('image title on hungarian'), max_length=50)
    title_en = models.CharField(_('image title on english'), max_length=50)
    gallery = models.ForeignKey(Gallery,
                                verbose_name=_('gallery'),
                                help_text=_('choose gallery'))
    date_uploaded = models.DateTimeField(_('date uploaded'), default=timezone.now)
    image = models.ImageField(_('image to be uploaded'),
                              upload_to='gallery/%Y/%m/%d')
    is_publishable = models.BooleanField(_('is image publishable?'),
                                         default=False)
    slug = models.SlugField()
    short_description_sr = models.CharField(_('short description on serbian'), max_length=256,
                                            help_text=_('shortly describe image'))
    short_description_hu = models.CharField(_('short description on hungarian'), max_length=256,
                                            help_text=_('shortly describe image'))
    short_description_en = models.CharField(_('short description on english'), max_length=256,
                                            help_text=_('shortly describe image'))
    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return self.title_sr
        elif translation.get_language() == 'hu':
            return self.title_hu
        elif translation.get_language() == 'en':
            return self.title_en
