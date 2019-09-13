from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query
from django.shortcuts import redirect, render
from tracking.models import Visitor, Pageview
from django.contrib.gis.geoip2 import GeoIP2


def search(request):
    search_query = request.GET.get('query', None)
    page = request.GET.get('page', 1)

    # Search
    if search_query:
        search_results = Page.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Page.objects.none()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })


def dashboard(request):
    dict_view = {}
    visitor_view = {}
    country_name = {}
    g = GeoIP2()
    for page in Pageview.objects.all():
        for filterpage in Pageview.objects.filter(url=page.url).distinct():
            dict_view.update({ filterpage.url: Pageview.objects.filter(url=page.url).count()})
    for visitor in Visitor.objects.all():
        try:
            visitor_view[(visitor.start_time).strftime("%Y-%m-%d")] += [visitor.session_key]
        except:
            visitor_view.update({(visitor.start_time).strftime("%Y-%m-%d"): [visitor.session_key]})
        if visitor.ip_address != request.META['REMOTE_ADDR']:
            try:
                country_name[g.city(visitor.ip_address)['country_name']] += [g.city(visitor.ip_address)['country_name']]
            except:
                country_name.update({g.city(visitor.ip_address)['country_name']: [g.city(visitor.ip_address)['country_name']]})
        else:
            pass

    return render(request, 'wagalytics/dashboard.html', {
        'pageview': dict_view,
        'visitor': visitor_view,
        'count_pageview': Pageview.objects.count(),
        'count_visitor': Visitor.objects.count(),
        'country_name': country_name,
    })
