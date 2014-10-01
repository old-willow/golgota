from django.db import models
from django.utils.translation import ugettext_lazy as _


class LinkCollections(models.Model):
    name = models.CharField(max_length=50,
                            help_text=_('Name used for link presentation.'))
    link = models.URLField(max_length=255,
                           help_text=_('Actual link'))
    date_created = models.DateTimeField(help_text=_('Date and time of item creation.'))
    date_modified = models.DateTimeField(blank=True, null=True,
                                         help_text=_('Date and time of item change.'))

    class Meta:
        ordering = ['date_created', ]
        verbose_name = _('link collection')
        verbose_name_plural = _('link collections')

    def __unicode__(self):
        return self.name
