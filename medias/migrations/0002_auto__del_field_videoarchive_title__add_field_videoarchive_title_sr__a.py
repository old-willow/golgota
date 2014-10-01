# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'VideoArchive.title'
        db.delete_column(u'medias_videoarchive', 'title')

        # Adding field 'VideoArchive.title_sr'
        db.add_column(u'medias_videoarchive', 'title_sr',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'VideoArchive.title_hu'
        db.add_column(u'medias_videoarchive', 'title_hu',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'VideoArchive.title_en'
        db.add_column(u'medias_videoarchive', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Deleting field 'AudioArchive.title'
        db.delete_column(u'medias_audioarchive', 'title')

        # Adding field 'AudioArchive.title_sr'
        db.add_column(u'medias_audioarchive', 'title_sr',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'AudioArchive.title_hu'
        db.add_column(u'medias_audioarchive', 'title_hu',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'AudioArchive.title_en'
        db.add_column(u'medias_audioarchive', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'VideoArchive.title'
        db.add_column(u'medias_videoarchive', 'title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Deleting field 'VideoArchive.title_sr'
        db.delete_column(u'medias_videoarchive', 'title_sr')

        # Deleting field 'VideoArchive.title_hu'
        db.delete_column(u'medias_videoarchive', 'title_hu')

        # Deleting field 'VideoArchive.title_en'
        db.delete_column(u'medias_videoarchive', 'title_en')

        # Adding field 'AudioArchive.title'
        db.add_column(u'medias_audioarchive', 'title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Deleting field 'AudioArchive.title_sr'
        db.delete_column(u'medias_audioarchive', 'title_sr')

        # Deleting field 'AudioArchive.title_hu'
        db.delete_column(u'medias_audioarchive', 'title_hu')

        # Deleting field 'AudioArchive.title_en'
        db.delete_column(u'medias_audioarchive', 'title_en')


    models = {
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
        u'medias.audioarchive': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'AudioArchive'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_published': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_leader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Staff']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_sr': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'medias.videoarchive': {
            'Meta': {'ordering': "['-date_published']", 'object_name': 'VideoArchive'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_published': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date_uploaded': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting_leader': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['home.Staff']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_sr': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['medias']