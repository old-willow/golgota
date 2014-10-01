# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.description'
        db.delete_column(u'events_event', 'description')

        # Deleting field 'Event.title'
        db.delete_column(u'events_event', 'title')

        # Deleting field 'Event.short_description'
        db.delete_column(u'events_event', 'short_description')

        # Adding field 'Event.title_sr'
        db.add_column(u'events_event', 'title_sr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Event.title_hu'
        db.add_column(u'events_event', 'title_hu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Event.title_en'
        db.add_column(u'events_event', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Event.short_description_sr'
        db.add_column(u'events_event', 'short_description_sr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Event.short_description_hu'
        db.add_column(u'events_event', 'short_description_hu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Event.short_description_en'
        db.add_column(u'events_event', 'short_description_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Event.description_sr'
        db.add_column(u'events_event', 'description_sr',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Event.description_hu'
        db.add_column(u'events_event', 'description_hu',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Event.description_en'
        db.add_column(u'events_event', 'description_en',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'Location.city'
        db.delete_column(u'events_location', 'city')

        # Deleting field 'Location.location_name'
        db.delete_column(u'events_location', 'location_name')

        # Deleting field 'Location.country'
        db.delete_column(u'events_location', 'country')

        # Adding field 'Location.country_sr'
        db.add_column(u'events_location', 'country_sr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Location.country_hu'
        db.add_column(u'events_location', 'country_hu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Location.country_en'
        db.add_column(u'events_location', 'country_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Location.city_sr'
        db.add_column(u'events_location', 'city_sr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Location.city_hu'
        db.add_column(u'events_location', 'city_hu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Location.city_en'
        db.add_column(u'events_location', 'city_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Location.location_name_sr'
        db.add_column(u'events_location', 'location_name_sr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Location.location_name_hu'
        db.add_column(u'events_location', 'location_name_hu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Location.location_name_en'
        db.add_column(u'events_location', 'location_name_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Deleting field 'Meeting.title'
        db.delete_column(u'events_meeting', 'title')

        # Adding field 'Meeting.title_sr'
        db.add_column(u'events_meeting', 'title_sr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Meeting.title_hu'
        db.add_column(u'events_meeting', 'title_hu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'Meeting.title_en'
        db.add_column(u'events_meeting', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'EventType.type'
        db.delete_column(u'events_eventtype', 'type')

        # Adding field 'EventType.type_sr'
        db.add_column(u'events_eventtype', 'type_sr',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'EventType.type_hu'
        db.add_column(u'events_eventtype', 'type_hu',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'EventType.type_en'
        db.add_column(u'events_eventtype', 'type_en',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Event.description'
        db.add_column(u'events_event', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Event.title'
        db.add_column(u'events_event', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Event.short_description'
        db.add_column(u'events_event', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Deleting field 'Event.title_sr'
        db.delete_column(u'events_event', 'title_sr')

        # Deleting field 'Event.title_hu'
        db.delete_column(u'events_event', 'title_hu')

        # Deleting field 'Event.title_en'
        db.delete_column(u'events_event', 'title_en')

        # Deleting field 'Event.short_description_sr'
        db.delete_column(u'events_event', 'short_description_sr')

        # Deleting field 'Event.short_description_hu'
        db.delete_column(u'events_event', 'short_description_hu')

        # Deleting field 'Event.short_description_en'
        db.delete_column(u'events_event', 'short_description_en')

        # Deleting field 'Event.description_sr'
        db.delete_column(u'events_event', 'description_sr')

        # Deleting field 'Event.description_hu'
        db.delete_column(u'events_event', 'description_hu')

        # Deleting field 'Event.description_en'
        db.delete_column(u'events_event', 'description_en')

        # Adding field 'Location.city'
        db.add_column(u'events_location', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Adding field 'Location.location_name'
        db.add_column(u'events_location', 'location_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Location.country'
        db.add_column(u'events_location', 'country',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Deleting field 'Location.country_sr'
        db.delete_column(u'events_location', 'country_sr')

        # Deleting field 'Location.country_hu'
        db.delete_column(u'events_location', 'country_hu')

        # Deleting field 'Location.country_en'
        db.delete_column(u'events_location', 'country_en')

        # Deleting field 'Location.city_sr'
        db.delete_column(u'events_location', 'city_sr')

        # Deleting field 'Location.city_hu'
        db.delete_column(u'events_location', 'city_hu')

        # Deleting field 'Location.city_en'
        db.delete_column(u'events_location', 'city_en')

        # Deleting field 'Location.location_name_sr'
        db.delete_column(u'events_location', 'location_name_sr')

        # Deleting field 'Location.location_name_hu'
        db.delete_column(u'events_location', 'location_name_hu')

        # Deleting field 'Location.location_name_en'
        db.delete_column(u'events_location', 'location_name_en')

        # Adding field 'Meeting.title'
        db.add_column(u'events_meeting', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'Meeting.title_sr'
        db.delete_column(u'events_meeting', 'title_sr')

        # Deleting field 'Meeting.title_hu'
        db.delete_column(u'events_meeting', 'title_hu')

        # Deleting field 'Meeting.title_en'
        db.delete_column(u'events_meeting', 'title_en')

        # Adding field 'EventType.type'
        db.add_column(u'events_eventtype', 'type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

        # Deleting field 'EventType.type_sr'
        db.delete_column(u'events_eventtype', 'type_sr')

        # Deleting field 'EventType.type_hu'
        db.delete_column(u'events_eventtype', 'type_hu')

        # Deleting field 'EventType.type_en'
        db.delete_column(u'events_eventtype', 'type_en')


    models = {
        u'events.event': {
            'Meta': {'ordering': "['-event_start_date']", 'object_name': 'Event'},
            'description_en': ('django.db.models.fields.TextField', [], {}),
            'description_hu': ('django.db.models.fields.TextField', [], {}),
            'description_sr': ('django.db.models.fields.TextField', [], {}),
            'event_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'event_end_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'event_start_date': ('django.db.models.fields.DateField', [], {}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['home.Staff']", 'null': 'True', 'blank': 'True'}),
            'host_church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.HostChurch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            'short_description_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_description_hu': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_description_sr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_sr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventType']"})
        },
        u'events.eventtype': {
            'Meta': {'object_name': 'EventType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_hu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type_sr': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'events.hostchurch': {
            'Meta': {'ordering': "['church']", 'object_name': 'HostChurch'},
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'events.location': {
            'Meta': {'ordering': "['city_sr']", 'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'city_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_hu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_sr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country_en': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country_hu': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country_sr': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_church': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'location_name_en': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'location_name_hu': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'location_name_sr': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'events.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.MeetingDay']"}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Staff']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_start': ('django.db.models.fields.TimeField', [], {}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title_sr': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.meetingday': {
            'Meta': {'object_name': 'MeetingDay'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.WeekDay']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'home.staff': {
            'Meta': {'ordering': "['date_registered']", 'object_name': 'Staff'},
            'about_me': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'date_registered': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'email_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fb_profile': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fb_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mob_phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'mob_phone_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'phone_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['home.StaffTitle']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'web_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'home.stafftitle': {
            'Meta': {'ordering': "['pk']", 'object_name': 'StaffTitle'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title_sr': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'home.weekday': {
            'Meta': {'object_name': 'WeekDay'},
            'day_en': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'day_hu': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'day_sr': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_regular_meeting_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['events']