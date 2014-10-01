from django.shortcuts import render, render_to_response
from django.template import RequestContext

from events.models import Location, HostChurch,  Event, EventType
from gallery.models import Gallery


def eventspage(request):
    """
    It should collect all events and check if events are passed and create two
    or three categoryies of events: 'passed' or 'yet to be' and 'currently taking place'.
    """
    #all_events = Event.objects.all()
    all_events = Event.objects.order_by('-event_start_date')
    #print(all_events, len(all_events))
    context = {
        'all_events': all_events,
    }
    return render_to_response('events/index.html',
                              context,
                              context_instance=RequestContext(request))


def latest_events(request):
    return render_to_response('events/index.html',
                              {},
                              context_instance=RequestContext(request))


def detail_event(request, id):
    event = Event.objects.get(id=id)

    # collect all galleries that points to this event.
    galleries = Gallery.objects.filter(event_id=id, is_publishable=True)

    # for testing!!!!!!!!
    #for gallery in galleries:
    #    print("Event id: " + str(event.id))
    #    print("Gallery name: " + unicode(gallery.name) + "; Gallery event id: " + unicode(gallery.event_id))

    context = {
        'event': event,
        'galleries': galleries,
    }

    return render_to_response('events/event-detail.html',
                              context,
                              context_instance=RequestContext(request))
