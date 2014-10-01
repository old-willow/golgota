# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'events_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country_sr', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('country_hu', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('country_en', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'events', ['Country'])

        # Adding model 'City'
        db.create_table(u'events_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Country'])),
            ('city_sr', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city_hu', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['City'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'events_country')

        # Deleting model 'City'
        db.delete_table(u'events_city')


    models = {
        u'events.city': {
            'Meta': {'ordering': "['city_sr']", 'object_name': 'City'},
            'city_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_hu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_sr': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'events.country': {
            'Meta': {'ordering': "['country_sr']", 'object_name': 'Country'},
            'country_en': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country_hu': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'country_sr': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
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
            'Meta': {'ordering': "['location_name_sr']", 'object_name': 'Location'},
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