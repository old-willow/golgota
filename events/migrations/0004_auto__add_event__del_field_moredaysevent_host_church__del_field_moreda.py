# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('host', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['home.Staff'], null=True, blank=True)),
            ('host_church', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.HostChurch'])),
            ('event_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Location'])),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255)),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Deleting field 'MoreDaysEvent.host_church'
        db.delete_column(u'events_moredaysevent', 'host_church_id')

        # Deleting field 'MoreDaysEvent.host'
        db.delete_column(u'events_moredaysevent', 'host_id')

        # Deleting field 'MoreDaysEvent.event_created'
        db.delete_column(u'events_moredaysevent', 'event_created')

        # Deleting field 'MoreDaysEvent.title'
        db.delete_column(u'events_moredaysevent', 'title')

        # Deleting field 'MoreDaysEvent.slug'
        db.delete_column(u'events_moredaysevent', 'slug')

        # Deleting field 'MoreDaysEvent.location'
        db.delete_column(u'events_moredaysevent', 'location_id')

        # Deleting field 'MoreDaysEvent.type'
        db.delete_column(u'events_moredaysevent', 'type_id')

        # Adding field 'MoreDaysEvent.event'
        db.add_column(u'events_moredaysevent', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Event']),
                      keep_default=False)

        # Deleting field 'OneDayEvent.host_church'
        db.delete_column(u'events_onedayevent', 'host_church_id')

        # Deleting field 'OneDayEvent.host'
        db.delete_column(u'events_onedayevent', 'host_id')

        # Deleting field 'OneDayEvent.event_created'
        db.delete_column(u'events_onedayevent', 'event_created')

        # Deleting field 'OneDayEvent.title'
        db.delete_column(u'events_onedayevent', 'title')

        # Deleting field 'OneDayEvent.slug'
        db.delete_column(u'events_onedayevent', 'slug')

        # Deleting field 'OneDayEvent.location'
        db.delete_column(u'events_onedayevent', 'location_id')

        # Adding field 'OneDayEvent.event'
        db.add_column(u'events_onedayevent', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Event']),
                      keep_default=False)

        # Adding field 'OneDayEvent.type'
        db.add_column(u'events_onedayevent', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.EventType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Adding field 'MoreDaysEvent.host_church'
        db.add_column(u'events_moredaysevent', 'host_church',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.HostChurch']),
                      keep_default=False)

        # Adding field 'MoreDaysEvent.host'
        db.add_column(u'events_moredaysevent', 'host',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['home.Staff']),
                      keep_default=False)

        # Adding field 'MoreDaysEvent.event_created'
        db.add_column(u'events_moredaysevent', 'event_created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'MoreDaysEvent.title'
        db.add_column(u'events_moredaysevent', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'MoreDaysEvent.slug'
        db.add_column(u'events_moredaysevent', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'MoreDaysEvent.location'
        db.add_column(u'events_moredaysevent', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Location']),
                      keep_default=False)

        # Adding field 'MoreDaysEvent.type'
        db.add_column(u'events_moredaysevent', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.EventType']),
                      keep_default=False)

        # Deleting field 'MoreDaysEvent.event'
        db.delete_column(u'events_moredaysevent', 'event_id')

        # Adding field 'OneDayEvent.host_church'
        db.add_column(u'events_onedayevent', 'host_church',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.HostChurch']),
                      keep_default=False)

        # Adding field 'OneDayEvent.host'
        db.add_column(u'events_onedayevent', 'host',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['home.Staff']),
                      keep_default=False)

        # Adding field 'OneDayEvent.event_created'
        db.add_column(u'events_onedayevent', 'event_created',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'OneDayEvent.title'
        db.add_column(u'events_onedayevent', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'OneDayEvent.slug'
        db.add_column(u'events_onedayevent', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'OneDayEvent.location'
        db.add_column(u'events_onedayevent', 'location',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['events.Location']),
                      keep_default=False)

        # Deleting field 'OneDayEvent.event'
        db.delete_column(u'events_onedayevent', 'event_id')

        # Deleting field 'OneDayEvent.type'
        db.delete_column(u'events_onedayevent', 'type_id')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'event_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['home.Staff']", 'null': 'True', 'blank': 'True'}),
            'host_church': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.HostChurch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Location']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        u'events.moredaysevent': {
            'Meta': {'ordering': "['-event_start']", 'object_name': 'MoreDaysEvent'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            'event_end': ('django.db.models.fields.DateField', [], {}),
            'event_start': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.onedayevent': {
            'Meta': {'ordering': "['-event_date']", 'object_name': 'OneDayEvent'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            'event_date': ('django.db.models.fields.DateField', [], {}),
            'event_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.EventType']"})
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