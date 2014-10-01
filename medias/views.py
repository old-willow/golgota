from django.shortcuts import render, render_to_response
from django.template import RequestContext

from medias.models import AudioArchive, VideoArchive


def mediaspage(request):
    # Page that will lead to archive page?

    return render_to_response('medias/index.html',
                             {},
                             context_instance=RequestContext(request))


def medias_archive(request):
    # list all archives for given year and month.
    audio_archives = AudioArchive.objects.filter(active=True)

    context = {
        'audio_archives': audio_archives,
    }

    return render_to_response('medias/archive-list.html',
                              context,
                              context_instance=RequestContext(request))
