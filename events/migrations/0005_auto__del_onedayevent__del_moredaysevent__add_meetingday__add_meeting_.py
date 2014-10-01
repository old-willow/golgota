# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'OneDayEvent'
        db.delete_table(u'events_onedayevent')

        # Deleting model 'MoreDaysEvent'
        db.delete_table(u'events_moredaysevent')

        # Adding model 'MeetingDay'
        db.create_table(u'events_meetingday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.WeekDay'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
        ))
        db.send_create_signal(u'events', ['MeetingDay'])

        # Adding model 'Meeting'
        db.create_table(u'events_meeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.MeetingDay'])),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Staff'])),
            ('time_start', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'events', ['Meeting'])

        # Adding field 'Event.type'
        db.add_column(u'events_event', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['events.EventType']),
                      keep_default=False)

        # Adding field 'Event.event_start_date'
        db.add_column(u'events_event', 'event_start_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 5, 22, 0, 0)),
                      keep_default=False)

        # Adding field 'Event.event_end_date'
        db.add_column(u'events_event', 'event_end_date',
                      self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Event.short_description'
        db.add_column(u'events_event', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Event.description'
        db.add_column(u'events_event', 'description',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding field 'Event.is_publishable'
        db.add_column(u'events_event', 'is_publishable',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'OneDayEvent'
        db.create_table(u'events_onedayevent', (
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('event_time', self.gf('django.db.models.fields.TimeField')()),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('event_date', self.gf('django.db.models.fields.DateField')()),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventType'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('is_publishable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'events', ['OneDayEvent'])

        # Adding model 'MoreDaysEvent'
        db.create_table(u'events_moredaysevent', (
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('event_end', self.gf('django.db.models.fields.DateField')()),
            ('is_publishable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('event_start', self.gf('django.db.models.fields.DateField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'events', ['MoreDaysEvent'])

        # Deleting model 'MeetingDay'
        db.delete_table(u'events_meetingday')

        # Deleting model 'Meeting'
        db.delete_table(u'events_meeting')

        # Deleting field 'Event.type'
        db.delete_column(u'events_event', 'type_id')

        # Deleting field 'Event.event_start_date'
        db.delete_column(u'events_event', 'event_start_date')

        # Deleting field 'Event.event_end_date'
        db.delete_column(u'events_event', 'event_end_date')

        # Deleting field 'Event.short_description'
        db.delete_column(u'events_event', 'short_description')

        # Deleting field 'Event.description'
        db.delete_column(u'events_event', 'description')

        # Deleting field 'Event.is_publishable'
        db.delete_column(u'events_event', 'is_publishable')


    models = {
        u'events.event': {
            'Meta': {'ordering': "['-event_start_date']", 'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'event_end_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'event_start_date': ('django.db.models.fields.DateField', [], {}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['home.Staff']", 'null': 'True', 'blank': 'True'}),
            'host_church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.HostChurch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventType']"})
        },
        u'events.eventtype': {
            'Meta': {'object_name': 'EventType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'events.hostchurch': {
            'Meta': {'ordering': "['church']", 'object_name': 'HostChurch'},
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'events.location': {
            'Meta': {'ordering': "['city']", 'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_church': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'events.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.MeetingDay']"}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Staff']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_start': ('django.db.models.fields.TimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'home.weekday': {
            'Meta': {'object_name': 'WeekDay'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_regular_meeting_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['events']