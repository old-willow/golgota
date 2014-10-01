from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from medias.models import AudioArchive, VideoArchive


class AudioArchiveAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Title'), {'fields': ('title_sr', 'title_hu', 'title_en', )}),
        (_('File stuff'), {'fields': ('meeting_leader', 'slug', 'file', )}),
        (_('Publishing Settings'), {'fields': ('active', 'date_published', )}),
        (_('Date Uploaded'), {'fields': ('date_uploaded', )}),
    )
    list_display = ('title_sr', 'active', 'date_published', 'meeting_leader', )
    list_display_links = ('title_sr', 'meeting_leader', )
    search_fields = ['title_sr', 'title_hu', 'title_en', 'active', ]
    prepopulated_fields = {'slug': ('title_en', ) }


class VideoArchiveAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Title'), {'fields': ('title_sr', 'title_hu', 'title_en', )}),
        (_('File stuff'), {'fields': ('meeting_leader', 'slug', 'file', )}),
        (_('Publishing Settings'), {'fields': ('active', 'date_published', )}),
        (_('Date Uploaded'), {'fields': ('date_uploaded', )}),
    )
    list_display = ('title_sr', 'active', 'date_published', 'meeting_leader', )
    list_display_links = ('title_sr', 'meeting_leader', )
    search_fields = ['title_sr', 'title_hu', 'title_en', 'active', ]
    prepopulated_fields = {'slug': ('title_en', ) }


admin.site.register(AudioArchive, AudioArchiveAdmin)
admin.site.register(VideoArchive, VideoArchiveAdmin)
