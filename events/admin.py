from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils import translation

from events.models import Country, City, Location, HostChurch, Event, EventType, Meeting

class CountryAdmin(admin.ModelAdmin):
    fields = ('country_sr', 'country_hu', 'country_en', )


class CityAdmin(admin.ModelAdmin):
    fields = ('country', 'city_sr', 'city_hu', 'city_en', )


class LocationAdmin(admin.ModelAdmin):
    fields = ( 'city',
              'location_name_sr', 'location_name_hu', 'location_name_en',
              'postal_code', 'address',
              'latitude', 'longitude', 'is_publishable', )


class HostChurchAdmin(admin.ModelAdmin):
    fields = ('name', 'church', 'is_publishable', )


class EventTypeAdmin(admin.ModelAdmin):
    fields = ('type_sr', 'type_hu', 'type_en', )


#if translation.get_language() == 'sr-latn':
#    title = 'title_sr'
#elif translation.get_language() == 'hu':
#    title = 'title_hu'
#elif translation.get_language() == 'en':
#    title = 'title_en'
#
#print("i am in events admin script " + str(title))

class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Basics'), {'fields': ('title_sr', 'title_hu', 'title_en', 'type',
                                  'host', 'host_church',
                                  'location', 'slug', 'is_publishable', )}),
        (_('Dates'), {'fields': ('event_created', 'event_start_date',
                                 'event_end_date', )}),
        (_('Descriptions'), {'fields': ('short_description_sr',
                                        'short_description_hu',
                                        'short_description_en',
                                        'description_sr',
                                        'description_hu',
                                        'description_en', )}),
    )
    list_display = ('type', 'title_sr', 'event_start_date', 'event_end_date',
                    'is_publishable', 'event_happen_in_time', )
    prepopulated_fields = {'slug': ('type', 'title_en', 'location', )}
    search_fields = ['meeting_type', 'title_sr', 'title_hu', 'title_en', 'location', ]


class MeetingAdmin(admin.ModelAdmin):
    fields = ('title_sr', 'title_hu', 'title_en', 'day', 'host', 'time_start')


admin.site.register(HostChurch, HostChurchAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Meeting, MeetingAdmin)
