from django.shortcuts import render, render_to_response
from django.template import RequestContext

from gallery.models import Gallery, Image


def gallery_home_page(request):
    gallery_list = Gallery.objects.filter(is_publishable=True)

    context = {
        'gallery_list': gallery_list,
    }

    return render_to_response('gallery/index.html',
                             context,
                             context_instance=RequestContext(request))



def gallery_page(request, gallery_id):
    """
    Collect all images that are publishable for the given gallery.
    """
    gallery = Gallery.objects.get(id=gallery_id)
    images = Image.objects.filter(is_publishable=True, gallery=gallery_id)

    context = {
        'gallery': gallery,
        'images': images,
    }
    return render_to_response('gallery/images-in-gallery.html',
                              context,
                              context_instance=RequestContext(request))
