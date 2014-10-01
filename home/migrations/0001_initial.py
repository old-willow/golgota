# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StaffTitle'
        db.create_table(u'home_stafftitle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'home', ['StaffTitle'])

        # Adding model 'Staff'
        db.create_table(u'home_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nickname', self.gf('django.db.models.fields.CharField')(default=None, max_length=10, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mob_phone', self.gf('django.db.models.fields.CharField')(default=None, max_length=30, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('about_me', self.gf('django.db.models.fields.TextField')(default=None, max_length=3000, null=True, blank=True)),
            ('date_registered', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'home', ['Staff'])

        # Adding M2M table for field title on 'Staff'
        m2m_table_name = db.shorten_name(u'home_staff_title')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staff', models.ForeignKey(orm[u'home.staff'], null=False)),
            ('stafftitle', models.ForeignKey(orm[u'home.stafftitle'], null=False))
        ))
        db.create_unique(m2m_table_name, ['staff_id', 'stafftitle_id'])

        # Adding model 'MeetingType'
        db.create_table(u'home_meetingtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meeting_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'home', ['MeetingType'])

        # Adding model 'WeekDay'
        db.create_table(u'home_weekday', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('is_regular_meeting_day', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'home', ['WeekDay'])

        # Adding model 'RegularMeeting'
        db.create_table(u'home_regularmeeting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.WeekDay'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('hour', self.gf('django.db.models.fields.TimeField')()),
            ('meeting_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.MeetingType'], null=True, blank=True)),
            ('meeting_leader', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Staff'])),
            ('is_weekly', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'home', ['RegularMeeting'])


    def backwards(self, orm):
        # Deleting model 'StaffTitle'
        db.delete_table(u'home_stafftitle')

        # Deleting model 'Staff'
        db.delete_table(u'home_staff')

        # Removing M2M table for field title on 'Staff'
        db.delete_table(db.shorten_name(u'home_staff_title'))

        # Deleting model 'MeetingType'
        db.delete_table(u'home_meetingtype')

        # Deleting model 'WeekDay'
        db.delete_table(u'home_weekday')

        # Deleting model 'RegularMeeting'
        db.delete_table(u'home_regularmeeting')


    models = {
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
            'meeting_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.MeetingType']", 'null': 'True', 'blank': 'True'})
        },
        u'home.staff': {
            'Meta': {'ordering': "['date_registered']", 'object_name': 'Staff'},
            'about_me': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '3000', 'null': 'True', 'blank': 'True'}),
            'date_registered': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'mob_phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.related.ManyToManyField', [], {'default': 'None', 'to': u"orm['home.StaffTitle']", 'null': 'True', 'symmetrical': 'False', 'blank': 'True'})
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

    complete_apps = ['home']