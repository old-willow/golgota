from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from datetime import datetime

from home.models import Staff, WeekDay
#from gallery.models import Gallery, Image
from medias.models import AudioArchive, VideoArchive


class Country(models.Model):
    country_sr = models.CharField(_('country on serbian'), max_length=150)
    country_hu = models.CharField(_('country on hungarian'), max_length=150)
    country_en = models.CharField(_('country on english'), max_length=150)

    class Meta:
        ordering = ['country_sr', ]
        verbose_name = _('country')
        verbose_name_plural = _('coutries')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u'%s' % (self.country_sr, )
        elif translation.get_language() == 'hu':
            return u'%s' % (self.country_hu, )
        elif translation.get_language() == 'en':
            return u'%s' % (self.country_en, )


class City(models.Model):
    country = models.ForeignKey(Country, verbose_name=_('choose country'))
    city_sr = models.CharField(_('city on serbian'), max_length=50)
    city_hu = models.CharField(_('city on hungarian'), max_length=50)
    city_en = models.CharField(_('city on english'), max_length=50)

    class Meta:
        ordering = ['city_sr', ]
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u'%s' % (self.city_sr, )
        elif translation.get_language() == 'hu':
            return u'%s' % (self.city_hu, )
        elif translation.get_language() == 'en':
            return u'%s' % (self.city_en, )


class Location(models.Model):
    #country_sr = models.CharField(_('country on serbian'), max_length=150)
    #country_hu = models.CharField(_('country on hungarian'), max_length=150)
    #country_en = models.CharField(_('country on english'), max_length=150)
    #city_sr = models.CharField(_('city on serbian'), max_length=50)
    #city_hu = models.CharField(_('city on hungarian'), max_length=50)
    #city_en = models.CharField(_('city on english'), max_length=50)
    #country = models.ForeignKey(Country, _('choose country'))
    city = models.ForeignKey(City, verbose_name=_('choose city'))
    location_name_sr = models.CharField(max_length=150,
                                        help_text=_("The name of the actual location where event will take place"))
    location_name_hu = models.CharField(max_length=150,
                                        help_text=_("The name of the actual location where event will take place"))
    location_name_en = models.CharField(max_length=150,
                                        help_text=_("The name of the actual location where event will take place"))
    postal_code = models.CharField(_('postal code'), max_length=15)
    address = models.CharField(_('address'), max_length=250)
    latitude = models.FloatField(blank=True, null=True, default=None)
    longitude = models.FloatField(blank=True, null=True, default=None)
    is_church = models.BooleanField(_('is this a church?'), default=False)
    is_publishable = models.BooleanField(_('is publishable?'), default=False)

    class Meta:
        ordering = ['location_name_sr', ]
        verbose_name = _('location')
        verbose_name_plural = _('locations')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u'%s; %s' % (self.location_name_sr, self.city.city_sr, )
        elif translation.get_language() == 'hu':
            return u'%s; %s' % (self.location_name_hu, self.city.city_hu, )
        elif translation.get_language() == 'en':
            return u'%s; %s' % (self.location_name_en, self.city.city_en, )


class HostChurch(models.Model):
    name = models.CharField(_('church name'), max_length=80)
    church = models.ForeignKey(Location, verbose_name=_('host church'))
    is_publishable = models.BooleanField(_('is publishable?'), default=False)

    class Meta:
        ordering = ['church', ]
        verbose_name = _('host church')
        verbose_name_plural = _('host churches')

    def __unicode__(self):
        return u'%s' % (self.name, )


class EventType(models.Model):
    type_sr = models.CharField(_('event on serbian'), max_length=50)
    type_hu = models.CharField(_('event on hungarian'), max_length=50)
    type_en = models.CharField(_('event on english'), max_length=50)

    class Meta:
        verbose_name = _('event type')
        verbose_name_plural = _('event types')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u'%s' % (self.type_sr, )
        elif translation.get_language() == 'hu':
            return u'%s' % (self.type_hu, )
        elif translation.get_language() == 'en':
            return u'%s' % (self.type_en, )


class Event(models.Model):
    title_sr = models.CharField(_('title on serbian'), max_length=200)
    title_hu = models.CharField(_('title on hungarian'), max_length=200)
    title_en = models.CharField(_('title on english'), max_length=200)
    type = models.ForeignKey(EventType, verbose_name=_('type of event'))
    host = models.ForeignKey(Staff, verbose_name=_('host person'),
                             blank=True, null=True, default=None)
    host_church = models.ForeignKey(HostChurch, verbose_name=_('host church'))
    event_created = models.DateTimeField(_('event created'),
                                         default=datetime.now,
                                         help_text='Database item created.')
    event_start_date = models.DateField(_('date when event starts'))
    # end date blank=True because maybe it is one day event.
    event_end_date = models.DateField(_('date when event ends'),
                                      blank=True, null=True, default=None)
    location = models.ForeignKey(Location)
    slug = models.SlugField(max_length=255)
    short_description_sr = models.CharField(_('short description on serbian'),
                                            max_length=255)
    short_description_hu = models.CharField(_('short description on hungarian'),
                                            max_length=255)
    short_description_en = models.CharField(_('short description on english'),
                                            max_length=255)
    description_sr = models.TextField(_('longer description on serbian'))
    description_hu = models.TextField(_('longer description on hungarian'))
    description_en = models.TextField(_('longer description on english'))
    is_publishable = models.BooleanField(_('is event publishable?'),
                                         default=False)

    class Meta:
        get_latest_by = 'event_start_date'
        ordering = ['-event_start_date', ]
        verbose_name = _('event')
        verbose_name_plural = _('events')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u'%s' % (self.title_sr, )
        elif translation.get_language() == 'hu':
            return u'%s' % (self.title_hu, )
        elif translation.get_language() == 'en':
            return u'%s' % (self.title_en, )

    def is_event_passed(self):
        now = timezone.now()
        if self.event_end_date == None:
            if now.date() > self.event_start_date:
                return True
        elif now.date() > self.event_end_date:
            return True
        else:
            return False

    def is_event_current(self):
        now = timezone.now()
        if now.date() >= self.event_start_date \
           and now.date() <= self.event_end_date:
            return True
        else:
            return False

    def is_event_future(self):
        now = timezone.now()
        if now.date() < self.event_start_date:
            return True
        else:
            return False

    def event_happen_in_time(self):
        passed = self.is_event_passed()
        if passed:
            return _('passed event')

        actual = self.is_event_current()
        if actual:
            return _('event currently takes place')

        future = self.is_event_future()
        if future:
            return _('future event')
    event_happen_in_time.short_description = _('event happen in time')


class MeetingDay(models.Model):
    date = models.DateField()
    day = models.ForeignKey(WeekDay)
    event = models.ForeignKey(Event)

    class Meta:
        verbose_name = _('meeting day')
        verbose_name_plural = _('meeting days')

    def __unicode__(self):
        return u'%s' % (self.day.day, )


class Meeting(models.Model):
    # I don't know why I created this model because it is not used anywhere.
    # I won't delete it yet, maybe later on it will just pop up in my mind why...
    title_sr = models.CharField(max_length=100)
    title_hu = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    day = models.ForeignKey(MeetingDay)
    host = models.ForeignKey(Staff)
    time_start = models.TimeField()

    class Meta:
        verbose_name = _('meeting')
        verbose_name_plural = _('meetings')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u'%s' % (self.title_sr, )
        elif translation.get_language() == 'hu':
            return u'%s' % (self.title_hu, )
        elif translation.get_language() == 'en':
            return u'%s' % (self.title_en, )
