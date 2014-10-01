# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'events_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('latitude', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('is_church', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_publishable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['Location'])

        # Adding model 'HostChurch'
        db.create_table(u'events_hostchurch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Location'])),
            ('is_publishable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['HostChurch'])

        # Adding model 'EventType'
        db.create_table(u'events_eventtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'events', ['EventType'])

        # Adding model 'OneDayEvent'
        db.create_table(u'events_onedayevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Staff'])),
            ('host_church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.HostChurch'])),
            ('event_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('event_date', self.gf('django.db.models.fields.DateField')()),
            ('event_time', self.gf('django.db.models.fields.TimeField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Location'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('is_publishable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['OneDayEvent'])

        # Adding model 'MoreDaysEvent'
        db.create_table(u'events_moredaysevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.EventType'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Staff'])),
            ('host_church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.HostChurch'])),
            ('event_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('event_start', self.gf('django.db.models.fields.DateField')()),
            ('event_end', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Location'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('is_publishable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['MoreDaysEvent'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'events_location')

        # Deleting model 'HostChurch'
        db.delete_table(u'events_hostchurch')

        # Deleting model 'EventType'
        db.delete_table(u'events_eventtype')

        # Deleting model 'OneDayEvent'
        db.delete_table(u'events_onedayevent')

        # Deleting model 'MoreDaysEvent'
        db.delete_table(u'events_moredaysevent')


    models = {
        u'events.eventtype': {
            'Meta': {'object_name': 'EventType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'events.hostchurch': {
            'Meta': {'ordering': "['church']", 'object_name': 'HostChurch'},
            'church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'events.location': {
            'Meta': {'ordering': "['city']", 'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_church': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'longitude': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'events.moredaysevent': {
            'Meta': {'ordering': "['-event_start']", 'object_name': 'MoreDaysEvent'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'event_end': ('django.db.models.fields.DateField', [], {}),
            'event_start': ('django.db.models.fields.DateField', [], {}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Staff']"}),
            'host_church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.HostChurch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventType']"})
        },
        u'events.onedayevent': {
            'Meta': {'ordering': "['-event_date']", 'object_name': 'OneDayEvent'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'event_date': ('django.db.models.fields.DateField', [], {}),
            'event_time': ('django.db.models.fields.TimeField', [], {}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Staff']"}),
            'host_church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.HostChurch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        }
    }

    complete_apps = ['events']