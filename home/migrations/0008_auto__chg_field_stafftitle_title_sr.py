# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StaffTitle.title_sr'
        db.alter_column(u'home_stafftitle', 'title_sr', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

    def backwards(self, orm):

        # Changing field 'StaffTitle.title_sr'
        db.alter_column(u'home_stafftitle', 'title_sr', self.gf('django.db.models.fields.CharField')(default='', max_length=30))

    models = {
        u'home.homepagecontent': {
            'Meta': {'object_name': 'HomePageContent'},
            'date_intro_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_services_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_statement_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro_en': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'intro_hu': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'intro_sr': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'services_en': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'services_hu': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'services_sr': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'statement_en': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'statement_hu': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'statement_sr': ('django.db.models.fields.TextField', [], {'max_length': '5000'})
        },
        u'home.meetingtype': {
            'Meta': {'object_name': 'MeetingType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'home.regularmeeting': {
            'Meta': {'ordering': "['day', 'hour']", 'object_name': 'RegularMeeting'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.WeekDay']"}),
            'hour': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_weekly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting_leader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Staff']"}),
            'meeting_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.MeetingType']", 'null': 'True', 'blank': 'True'}),
            'ml_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
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
            'title_sr': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'home.weekday': {
            'Meta': {'object_name': 'WeekDay'},
            'day': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_regular_meeting_day': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['home']