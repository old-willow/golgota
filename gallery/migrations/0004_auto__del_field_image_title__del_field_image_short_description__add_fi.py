# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.title'
        db.delete_column(u'gallery_image', 'title')

        # Deleting field 'Image.short_description'
        db.delete_column(u'gallery_image', 'short_description')

        # Adding field 'Image.title_sr'
        db.add_column(u'gallery_image', 'title_sr',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Image.title_hu'
        db.add_column(u'gallery_image', 'title_hu',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Image.title_en'
        db.add_column(u'gallery_image', 'title_en',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Image.short_description_sr'
        db.add_column(u'gallery_image', 'short_description_sr',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Adding field 'Image.short_description_hu'
        db.add_column(u'gallery_image', 'short_description_hu',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Adding field 'Image.short_description_en'
        db.add_column(u'gallery_image', 'short_description_en',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Deleting field 'Gallery.description'
        db.delete_column(u'gallery_gallery', 'description')

        # Deleting field 'Gallery.name'
        db.delete_column(u'gallery_gallery', 'name')

        # Deleting field 'Gallery.short_description'
        db.delete_column(u'gallery_gallery', 'short_description')

        # Adding field 'Gallery.name_sr'
        db.add_column(u'gallery_gallery', 'name_sr',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Gallery.name_hu'
        db.add_column(u'gallery_gallery', 'name_hu',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Gallery.name_en'
        db.add_column(u'gallery_gallery', 'name_en',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Gallery.short_description_sr'
        db.add_column(u'gallery_gallery', 'short_description_sr',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Adding field 'Gallery.short_description_hu'
        db.add_column(u'gallery_gallery', 'short_description_hu',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Adding field 'Gallery.short_description_en'
        db.add_column(u'gallery_gallery', 'short_description_en',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Adding field 'Gallery.description_sr'
        db.add_column(u'gallery_gallery', 'description_sr',
                      self.gf('django.db.models.fields.TextField')(default=None, max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.description_hu'
        db.add_column(u'gallery_gallery', 'description_hu',
                      self.gf('django.db.models.fields.TextField')(default=None, max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.description_en'
        db.add_column(u'gallery_gallery', 'description_en',
                      self.gf('django.db.models.fields.TextField')(default=None, max_length=2000, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Image.title'
        db.add_column(u'gallery_image', 'title',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Adding field 'Image.short_description'
        db.add_column(u'gallery_image', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Deleting field 'Image.title_sr'
        db.delete_column(u'gallery_image', 'title_sr')

        # Deleting field 'Image.title_hu'
        db.delete_column(u'gallery_image', 'title_hu')

        # Deleting field 'Image.title_en'
        db.delete_column(u'gallery_image', 'title_en')

        # Deleting field 'Image.short_description_sr'
        db.delete_column(u'gallery_image', 'short_description_sr')

        # Deleting field 'Image.short_description_hu'
        db.delete_column(u'gallery_image', 'short_description_hu')

        # Deleting field 'Image.short_description_en'
        db.delete_column(u'gallery_image', 'short_description_en')

        # Adding field 'Gallery.description'
        db.add_column(u'gallery_gallery', 'description',
                      self.gf('django.db.models.fields.TextField')(default=None, max_length=2000, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Gallery.name'
        db.add_column(u'gallery_gallery', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)

        # Adding field 'Gallery.short_description'
        db.add_column(u'gallery_gallery', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)

        # Deleting field 'Gallery.name_sr'
        db.delete_column(u'gallery_gallery', 'name_sr')

        # Deleting field 'Gallery.name_hu'
        db.delete_column(u'gallery_gallery', 'name_hu')

        # Deleting field 'Gallery.name_en'
        db.delete_column(u'gallery_gallery', 'name_en')

        # Deleting field 'Gallery.short_description_sr'
        db.delete_column(u'gallery_gallery', 'short_description_sr')

        # Deleting field 'Gallery.short_description_hu'
        db.delete_column(u'gallery_gallery', 'short_description_hu')

        # Deleting field 'Gallery.short_description_en'
        db.delete_column(u'gallery_gallery', 'short_description_en')

        # Deleting field 'Gallery.description_sr'
        db.delete_column(u'gallery_gallery', 'description_sr')

        # Deleting field 'Gallery.description_hu'
        db.delete_column(u'gallery_gallery', 'description_hu')

        # Deleting field 'Gallery.description_en'
        db.delete_column(u'gallery_gallery', 'description_en')


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
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.City']"}),
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
        u'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description_en': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'description_hu': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'description_sr': ('django.db.models.fields.TextField', [], {'default': 'None', 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['events.Event']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_hu': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_sr': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_description_en': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'short_description_hu': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'short_description_sr': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            'date_uploaded': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_publishable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'short_description_en': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'short_description_hu': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'short_description_sr': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_sr': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        }
    }

    complete_apps = ['gallery']