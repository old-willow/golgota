from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from home.models import StaffTitle, Staff, RegularMeeting, MeetingType, WeekDay, HomePageContent
from home.forms import StaffForm


class StaffTitleAdmin(admin.ModelAdmin):
    pass


class StaffAdmin(admin.ModelAdmin):
    form = StaffForm
    fieldsets = (
        ('Basic', {'fields': ('first_name', 'last_name', 'nickname', 'slug', )}),
        ('Profile Image', {'fields': ('image', 'image_publishable', )}),
        ('Phone', {'fields': ('phone', 'phone_publishable', 'mob_phone', 'mob_phone_publishable', )}),
        ('Web', {'fields': ('web', 'web_publishable', 'email', 'email_publishable',
                            'fb_profile', 'fb_publishable', )}),
        ('Date Registered', {'fields': ('date_registered', )}),
        ('Other', {'fields': ('title', 'about_me', )}),
    )
    prepopulated_fields = {'slug': ('nickname', ) }


#class MeetingTimeAdmin(admin.ModelAdmin):
#    fields = ('hour', )


class MeetingTypeAdmin(admin.ModelAdmin):
    fields = ('meeting_name_sr', 'meeting_name_hu', 'meeting_name_en', )


class WeekDayAdmin(admin.ModelAdmin):
    fields = ('day_sr', 'day_hu', 'day_en', 'is_regular_meeting_day', )
    list_display = ('day_sr', 'day_hu', 'day_en', 'is_regular_meeting_day', )
    list_editable = ('is_regular_meeting_day', )


class RegularMeetingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Meeting and Leader', {'fields': ('meeting_type', 'meeting_leader', 'is_weekly', )}),
        ('Time Provided', {'classes': ('extrapritty', ), 'fields': (('date', 'hour', 'day', ), )}),
    )
    # fields that are present on the change list admin page.
    list_display = ('meeting_type', 'meeting_leader', 'date', 'day', 'hour', 'is_weekly', )
    #list_display = ('meeting_type', 'date', 'day', 'hour', )
    list_editable = ('is_weekly', )

    #list_display_links = ('meeting_type', 'meeting_leader', )
    list_filter = ('meeting_leader', )
    search_fields = ['meeting_type', 'meeting_leader', ]


#class HPCAdminInline(admin.TabularInline):
#    model = HomePageContent

class HomePageContentAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Introduction'), {'fields': (('intro_sr', 'intro_hu', 'intro_en', ), 'date_intro_changed', )}),
        (_('Statement'), {'fields': (('statement_sr', 'statement_hu', 'statement_en', ), 'date_statement_changed', )}),
        (_('Services'), {'fields': (('services_sr', 'services_hu', 'services_en', ), 'date_services_changed', )}),
        #(_('Change Dates'), {'fields': ('date_intro_changed',
        #                                'date_statement_changed',
        #                                'date_services_changed', )}), )
    )
    #inlines = [HPCAdminInline, ]



admin.site.register(StaffTitle, StaffTitleAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(RegularMeeting, RegularMeetingAdmin)
admin.site.register(MeetingType, MeetingTypeAdmin)
admin.site.register(WeekDay, WeekDayAdmin)
admin.site.register(HomePageContent, HomePageContentAdmin)
#admin.site.register(MeetingTime, MeetingTimeAdmin)
