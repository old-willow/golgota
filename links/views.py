from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from links.models import LinkCollections


def linkspage(request):
    all_links = LinkCollections.objects.all()
    context = { 'all_links': all_links }

    return render_to_response('links/index.html',
                              context,
                              context_instance=RequestContext(request))
