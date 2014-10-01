from django.utils.translation import ugettext_lazy as _

from django.db import models


class Contacts(models.Model):
    name = models.CharField(_('full name'), max_length=50,
                            help_text=_('Full name please.'))
    email = models.EmailField(_('valid email'), help_text=_('Type a valid email.'))
    subject = models.CharField(_('subject'), max_length=100,
                               help_text=_('Type short topic.'))
    message = models.TextField(_('message'),max_length=2000,
                               help_text=_('Type Your message.'))
    date_submited = models.DateTimeField(_('date submited'))
    web_site = models.URLField(_('web site'), blank=True, null=True,
                               help_text=_('Optional. Your Web Site.'))

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        get_latest_by = 'date_submited'

    def __unicode__(self):
        return self.email
