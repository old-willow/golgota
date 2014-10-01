from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.utils import translation

import datetime

from home.models import Staff, RegularMeeting, HomePageContent
from events.models import Event

# {{{
def run_through_week_days_blueprint(wm):
    """
    NOT USED, ONLY BLUEPRINT
    wm -> weekly_meetings
    Blueprint function that runs trough week days of current day week.
    And collects all of them in a list.
    """
    MAX_DAYS_OF_WEEK = 6 + 1
    current_week = []

    today = datetime.date.today()
    print('today is', str(today.weekday()))

    for i in xrange(0, MAX_DAYS_OF_WEEK):
        if i < today.weekday():
            day = today - datetime.timedelta(days=today.weekday() - i)
            current_week.append(day)

        if i == today.weekday():
            current_week.append(today)

        if i > today.weekday():
            day = today + datetime.timedelta(days=i - today.weekday())
            current_week.append(day)

    for cd in current_week:
        print(str(cd))

    return current_week
# }}}


def run_through_week_days(wm):
    """
    wm -> weekly_meetings
    Function that collects dates for [wm] days in a current week.
    And collects all of them in a list.
    Database table has weekdays pk start from 1.
    """
    MAX_DAYS_OF_WEEK = 6 + 1
    NUMBER_OF_MEETINGS_PER_WEEK = len(wm)
    current_week = []
    meeting_dates = []

    today = datetime.date.today()
    #print('today is', str(today.weekday()))

    # Collect current week dates from Monday to Sunday.
    for i in xrange(0, MAX_DAYS_OF_WEEK):
        if i < today.weekday():
            day = today - datetime.timedelta(days=today.weekday() - i)
            current_week.append(day)

        if i == today.weekday():
            current_week.append(today)

        if i > today.weekday():
            day = today + datetime.timedelta(days=i - today.weekday())
            current_week.append(day)

    for meeting in wm:
        for i in xrange(MAX_DAYS_OF_WEEK):
            if meeting.day_id == i + 1:
                meeting_dates.append(current_week[i])

    return meeting_dates


def meeting_date_generator(dates):
    """
    Simple generator for looping over dates for regular weekly meetings.
    """
    for item in dates:
        yield item


def homepage(request):
    print(translation.get_language())
    #print(request.LANGUAGE_CODE)  #  Same as above.
    weekly_meetings = RegularMeeting.objects.filter(is_weekly=True)
    other_meetings = RegularMeeting.objects.filter(is_weekly=False)
    #home_page_content = HomePageContent.objects.get(pk=1)
    #print("home page content: " + str(home_page_content));
    #print('other meeting len: ' + str(other_meetings))
    #print("session.django_language:" + request.session['django_language'])
    #for i in request.session:
    #    print(i)
    #request.session['django_language'] = 'hu'
    #print(request.session['django_language'])
    #print(request.META['HTTP_ACCEPT_LANGUAGE'])

    # Just for testing.
    #for i in weekly_meetings:
    #    print(i.day.id)

    #print settings.LOCALE_PATHS[0]

    meeting_dates = run_through_week_days(weekly_meetings)
    #dates = MeetingDateGenerator(meeting_dates)
    dates = meeting_date_generator(meeting_dates)
    #print('date: ' + str(dates.next()))
    #for d in dates:
    #    print(d)
    #print dates.next()

    field_names = []
    for name in RegularMeeting._meta.fields:
        field_names.append(name.verbose_name)

    # Check if there is current or future event.
    # Provide link to those.
    events_all = Event.objects.all()
    events_filtered = []
    if events_all:
        for e in events_all:
            # if e.is_event_current or e.is_event_future:
            print(e)
            print("is event passed " + str(e.is_event_passed()))
            if not e.is_event_passed():
                events_filtered.append(e)
    print("number of all events " + str(len(events_all)))
    print("number of filtered events " + str(len(events_filtered)))
    #print(event_currentt)
    #event_current = Event.objects.filter(is_event_current=True)
    #event_future  = Event.objects.filter(is_event_future=True)
    #print(type(event_current))
    #print(type(event_future))
    #event_current = []
    #event_future = []
    #for ec in tmp_event_current:
    #    if ec.event_happen_in_time == 'event currently takes place':
    #        event_current.append(ec)
    #for ef in tmp_event_future:
    #    if ef.event_happen_in_time == 'future event':
    #        event_future.append(ef)

    context = {
        'weekly_meetings': weekly_meetings,
        'dates': dates,
        'meeting_dates': meeting_dates,
        'other_meetings': other_meetings,
        'field_names': field_names,
        'events_filtered': events_filtered,
        #'content': home_page_content,
    }

    return render_to_response('home/index.html',
                              context,
                              context_instance=RequestContext(request))


def staff_detail(request, slug):
    staff = Staff.objects.get(slug=slug)
    context = {
        'staff': staff,
    }
    return render_to_response('home/detail-staff.html',
                              context,
                              context_instance=RequestContext(request))


# vim foldmethod=marker
