from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from home.models import Staff

from datetime import datetime


class AudioArchive(models.Model):
    title_sr = models.CharField(_('audio archive title on serbian'), max_length=255)
    title_hu = models.CharField(_('audio archive title on hungarian'), max_length=255)
    title_en = models.CharField(_('audio archive title on english'), max_length=255)
    slug = models.SlugField()
    date_published = models.DateField(_('publishing date'), blank=True,
                                      null=True, default=None)
    date_uploaded = models.DateField(_('upload date'), default=datetime.now)
    active = models.BooleanField(_('is publishable?'), default=False)
    file = models.FileField(_('audio file'), upload_to='archive/audio/%Y/%m/%d/')
    meeting_leader = models.ForeignKey(Staff, verbose_name=_('meeting leader'))

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return self.title_sr
        elif translation.get_language() == 'hu':
            return self.title_hu
        elif translation.get_language() == 'en':
            return self.title_en

    class Meta:
        ordering = ['-date_published', ]
        verbose_name = _('audio archive')
        verbose_name_plural = _('audio archives')


class VideoArchive(models.Model):
    title_sr = models.CharField(_('video archive title on serbian'), max_length=255)
    title_hu = models.CharField(_('video archive title on hungarian'), max_length=255)
    title_en = models.CharField(_('video archive title on english'), max_length=255)
    slug = models.SlugField()
    date_published = models.DateField(_('publishing date'), blank=True,
                                      null=True, default=None)
    date_uploaded = models.DateField(_('upload date'), default=datetime.now)
    active = models.BooleanField(_('is publishable?'), default=False)
    file = models.FileField(_('audio file'), upload_to='archive/video/%Y/%m/%d/')
    meeting_leader = models.ForeignKey(Staff, verbose_name=_('meeting leader'))

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return self.title_sr
        elif translation.get_language() == 'hu':
            return self.title_hu
        elif translation.get_language() == 'en':
            return self.title_en

    class Meta:
        ordering = ['-date_published', ]
        verbose_name = _('video archive')
        verbose_name_plural = _('video archives')
