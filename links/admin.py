from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from links.models import LinkCollections


class LinkCollectionsAdmin(admin.ModelAdmin):
    fields = ['name', 'link', 'date_created', 'date_modified']

admin.site.register(LinkCollections, LinkCollectionsAdmin)
