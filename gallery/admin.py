from django.contrib import admin
from django.utils.translation import ugettext as _

from gallery.models import Gallery, Image
from gallery.forms import ImageForm


#class ImageInline(admin.TabularInline):
class ImageInline(admin.StackedInline):
    model = Image
    extra = 3


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Image name'), {'fields': ('name_sr', 'name_hu', 'name_en', )}),
        (_('Image description'), {'fields': ('short_description_sr',
                                             'short_description_hu',
                                             'short_description_en',
                                             'description_sr',
                                             'description_hu',
                                             'description_en', )}),
        (_('Other settings'), {'fields': ('date_created', 'event', 'slug', 'is_publishable', )}),
    )
    list_display = ('name_sr', 'date_created', 'event', 'is_publishable', )
    prepopulated_fields = {'slug': ('name_en', 'event', )}
    search_fields = ['name_sr', 'name_hu', 'name_en', 'event', ]
    inlines = [ImageInline, ]


class ImageAdmin(admin.ModelAdmin):
    form = ImageForm
    fieldsets = (
        (_('Image title'), {'fields': ('title_sr', 'title_hu', 'title_en', )}),
        (_('File'), {'fields': ('image', )}),
        (_('Description'), {'fields': ('short_description_sr',
                                       'short_description_hu',
                                       'short_description_en', )}),
        (_('Other settings'), {'fields': ('gallery', 'slug','is_publishable',  )}),
        (_('Date'), {'fields': ('date_uploaded', )}),
    )
    list_display = ('title_sr', 'gallery', 'date_uploaded', 'is_publishable', )
    prepopulated_fields = {'slug': ('title_en', 'gallery', )}
    search_fields = ['title_sr', 'title_hu', 'title_en', 'gallery', ]


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
