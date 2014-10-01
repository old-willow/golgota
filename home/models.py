# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.utils.encoding import smart_unicode

from datetime import datetime

# I found this article to be so far the best explaination for translating:
#http://stackoverflow.com/questions/18392405/issue-trying-to-change-language-from-django-template
# This works for me now. But it seems to me that this is not how the
# documentation explains, or I don't understed. Maybe .

STAFFTITLES = (
    (u'01', _(u'Pastor')),
    (u'02', _(u'Učitelj')),
    (u'03', _(u'Đakon')),
    (u'04', _(u'Vođa slavljenja')),
    (u'05', _(u'Član tima za slavljenje')),
    (u'06', _(u'Pomoćnik')),
    (u'07', _(u'Volunter')),
    (u'08', _(u'Prevodilac')),
    (u'09', _(u'Gost')),
)


# Translators: Staff Title model.
class StaffTitle(models.Model):
    title_sr = models.CharField(_('rank on serbian'), max_length=30,
                                blank=True, null=True, default=None)
    title_hu = models.CharField(_('rank on hungarian'), max_length=30,
                                blank=True, null=True, default=None)
    title_en = models.CharField(_('rank on english'), max_length=30,
                                blank=True, null=True, default=None)

    class Meta:
        ordering = ['pk', ]
        verbose_name = _('staff rank')
        verbose_name_plural = _('staff ranks')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return self.title_sr
        elif translation.get_language() == 'hu':
            return self.title_hu
        elif translation.get_language() == 'en':
            return self.title_en


# Translators: Staff model.
class Staff(models.Model):
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    nickname = models.CharField(_('nickname'), max_length=10,
                                blank=True, null=True, default=None)
    #slug = models.SlugField(blank=True, null=True, default=None)
    slug = models.SlugField()

    image = models.ImageField(_('staff portrait image'),
                              upload_to='images/staff-portraits/',
                              help_text=_('Only \'jpg\', \'gif\'  and \'png\' image files allowed under 2.5 MB size!'),
                              blank=True, null=True, default=None)
    image_publishable = models.BooleanField(_('is image publishable?'),
                                            default=True)

    email = models.EmailField()
    email_publishable = models.BooleanField(_('is email publishable?'),
                                            default=False)

    web = models.URLField(_('web page'), max_length=200,
                          blank=True, null=True, default=None)
    web_publishable = models.BooleanField(_('is web page publishable?'),
                                          default=True)

    fb_profile = models.URLField(_('facebook profile page'), max_length=200,
                                 blank=True, null=True, default=None)
    fb_publishable = models.BooleanField(_('is facebook web page publishable?'),
                                         default=True)

    mob_phone = models.CharField(_('mobile phone'), max_length=30,
                                 blank=True, null=True, default=None)
    mob_phone_publishable = models.BooleanField(_('is mobile phone number publishable?'),
                                                default=False)

    phone = models.CharField(_('phone'), max_length=30, blank=True, null=True)
    phone_publishable = models.BooleanField(_('is phone number publishable?'),
                                            default=False)

    title = models.ManyToManyField(StaffTitle, verbose_name=_('title'),
                                   blank=True, null=True, default=None)
    about_me = models.TextField(_('about me'), max_length=3000,
                                blank=True, null=True, default=None)
    date_registered = models.DateTimeField(_('date registered'),
                                           default=datetime.now)  #, blank=True)

    class Meta:
        ordering = ['date_registered', ]
        verbose_name = _('staff')
        verbose_name_plural = _('staffs')

    def get_title(self):
        print(type(self.title))
        return '%s' % (self.title, )
    get_title.short_description = _('Get me a title of staff.')

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name, )

def get_meeting_leader():
    """
    This function is for geting default value for the field meeting_leader in
    RegularMeeting model.
    """
    return Staff.objects.get(pk=1)

# Translators: Days of the Week.
WEEKDAYS = (
    ('MON', _('Ponedeljak')),
    ('TUE', _('Utorak')),
    ('WED', _('Sreda')),
    ('THU', _('Četvrtak')),
    ('FRI', _('Petak')),
    ('SAT', _('Subota')),
    ('SUN', _('Nedelja')),
)
#WEEKDAYS = (
#    ('MON', _('Monday')),
#    ('TUE', _('Tuesday')),
#    ('WED', _('Wednesday')),
#    ('THU', _('Thursday')),
#    ('FRI', _('Friday')),
#    ('SAT', _('Saturday')),
#    ('SUN', _('Sunday')),
#)

# Translators: Meeting types.
MEETING_TYPES = (
    ('NONE', _('Nema sastanka')),
    ('STUDY', _('Biblijski čas')),
    ('PRAY', _('Molitveni čas')),
    ('WORSHIP', _('Slavljenje')),
    ('MALE', _('Muški čas')),
    ('FEMALE', _('Ženski čas')),
    ('HOME', _('Kučno zajedništvo')),
#    ('NONE', _('No meeting')),
#    ('STUDY', _('Bible study')),
#    ('PRAY', _('Prayer meeting')),
#    ('WORSHIP', _('Worship meeting')),
#    ('MALE', _('Men meeting')),
#    ('FEMALE', _('Women meeting')),
#    ('HOME', _('Home meeting')),
)


#  Translators: MeetingType model
class MeetingType(models.Model):
    meeting_name_sr = models.CharField(_('meeting name on serbian'),
                                       max_length=50, blank=True,
                                       null=True, default=None)
    meeting_name_hu = models.CharField(_('meeting name on hungarian'),
                                       max_length=50, blank=True,
                                       null=True, default=None)
    meeting_name_en = models.CharField(_('meeting name on english'),
                                       max_length=50, blank=True,
                                       null=True, default=None)

    class Meta:
        #order_with_respect_to = 'day'  # This is almost always used with related objects.
        verbose_name = _('meeting type')
        verbose_name_plural = _('meeting types')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u"%s" % self.meeting_name_sr
        elif translation.get_language() == 'hu':
            return u"%s" % self.meeting_name_hu
        elif translation.get_language() == 'en':
            return u"%s" % self.meeting_name_en

def get_meeting_type():
    """
    This function is used only for setting default value for
    RegularMeeting->meeting_type field, south requires it for default value.
    """
    return MeetingType.objects.get(pk=1)


#  Translators: WeekDay model
class WeekDay(models.Model):
    day_sr = models.CharField(_('day on serbian'), max_length=15,
                              blank=True, null=True, default=None)
    day_hu = models.CharField(_('day on hungarian'), max_length=15,
                              blank=True, null=True, default=None)
    day_en = models.CharField(_('day on english'), max_length=15,
                              blank=True, null=True, default=None)
    is_regular_meeting_day = models.BooleanField(_('is regular meeting day?'), default=False)

    class Meta:
        #order_with_respect_to = 'day'  # This is almost always used with related objects.
        verbose_name = _('week day')
        verbose_name_plural = _('week days')

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return u'%s' % self.day_sr
        elif translation.get_language() == 'hu':
            return u'%s' % self.day_hu
        elif translation.get_language() == 'en':
            return u'%s' % self.day_en


#  Translators: RegularMeeting model
class RegularMeeting(models.Model):
    """
    Regular meeting was first intended to be for only weekly
    meetings. After some time I realised there is no point to
    create another model for non regular meetings. So is_weekly
    field is enough to mark it as regular meeting or not.

    Changing RegularMeeting class name to only Meeting will be considered.

    When defining non reqular meetings always add date manually to the item.
    """
    day = models.ForeignKey(WeekDay, verbose_name=_('meeting day'))
    date = models.DateField(_('meeting date'), blank=True, null=True, default=None)  # This is necessary, not every meeting is weekly.
    hour = models.TimeField(_('hour of meeting'))
    meeting_type = models.ForeignKey(MeetingType,
                                     verbose_name=_('meeting category'),
                                     blank=True, null=True,
                                     # default=get_meeting_type)  # previous setting.
                                     default=None)
    #meeting_type = models.CharField(_('fellowship meeting category'), max_length=10, choices=MEETING_TYPES)
    meeting_leader = models.ForeignKey(Staff, verbose_name=_('meeting leader'),
                                       default=get_meeting_leader)
    ml_publishable = models.BooleanField(_('is meeting leader publishable?'),
                                         default=True)
    is_weekly = models.BooleanField(_('is weekly meeting?'), default=False)

    class Meta:
        #order_with_respect_to = 'day'  # This is almost always used with related objects.
        ordering = ['day', 'hour', ]
        verbose_name = _('regular meeting')
        verbose_name_plural = _('regular meetings')

    def get_if_meeting_day(self):
        # So far as I see this is a stupid function. Doesn't do anything useful!!!
        current_day = datetime.now().day
        print('current_day:', current_day)
        return current_day

    def get_day(self):
        if translation.get_language() == 'sr-latn':
            return self.day.day_sr
        if translation.get_language() == 'hu':
            return self.day.day_hu
        if translation.get_language() == 'en':
            return self.day.day_en
    get_day.short_description = _('Return me a day.')

    def is_weekly_meeting(self):
        return self.is_weekly
    is_weekly_meeting.short_description = _('is this a weekly meeting?')

    def get_meeting_leader_templates(self):
        return '%s' % (self.meeting_leader.slug, )

    def get_title(self):
        return '%s' % (self.meeting_leader.title, )
    #def get_field_name(self):
    #    return self._meta.field
    get_title.short_description = _('Get me a title of staff.')

    def get_meeting_type(self):
        if translation.get_language() == 'sr-latn':
            return u'%s' % (self.meeting_type.meeting_name_sr, )
        if translation.get_language() == 'hu':
            return u'%s' % (self.meeting_type.meeting_name_hu, )
        if translation.get_language() == 'en':
            return u'%s' % (self.meeting_type.meeting_name_en, )

    def __unicode__(self):
        # REMINDER: Every field that has choices set, the object will have a
        # get_FOO_display() mehtod, where FOO is the name of the filed.
        # This method return human readable value of the field.
    #    return self.get_meeting_type_display()
        return u'%s, %s' %  (self.day, self.meeting_type, )


#  Translators: HomePageContent model
class HomePageContent(models.Model):
    intro_en = models.TextField(_('introduction on english'), max_length=5000)
    intro_sr = models.TextField(_('introduction on serbian'), max_length=5000)
    intro_hu = models.TextField(_('introduction on hungarian'), max_length=5000)
    date_intro_changed = models.DateTimeField(default=datetime.now)

    statement_en = models.TextField(_('statement on english'), max_length=5000)
    statement_sr = models.TextField(_('statement on serbian'), max_length=5000)
    statement_hu = models.TextField(_('statement on hungarian'), max_length=5000)
    date_statement_changed = models.DateTimeField(default=datetime.now)

    services_en = models.TextField(_('services on english'), max_length=5000)
    services_sr = models.TextField(_('services on serbian'), max_length=5000)
    services_hu = models.TextField(_('services on hungarian'), max_length=5000)
    date_services_changed = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        if translation.get_language() == 'sr-latn':
            return self.intro_sr
        if translation.get_language() == 'hu':
            return self.intro_hu
        if translation.get_language() == 'en':
            return self.intro_en

    class Meta:
        verbose_name = _('home page content')
        verbose_name_plural = _('home page contents')

# vim: foldmethod=manual
