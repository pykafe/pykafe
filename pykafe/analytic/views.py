from django.shortcuts import render
from tracking.models import Visitor, Pageview
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError


def dashboard(request):
    page_view = {}
    visitor_view = {}
    country_name = {}
    count_users = {}
    geolocation = {}
    g = GeoIP2()
    for page in Pageview.objects.distinct():
        pages =  Pageview.objects.filter(url=page.url)
        try:
            page_view[page.url] += pages.count()
        except KeyError as e:
            page_view.update({page.url: pages.count()})
    for visitor in Visitor.objects.distinct():
        try:
            visitor_view[(visitor.start_time).strftime("%Y-%m-%d")] += [visitor.session_key]
            country_name[g.city(visitor.ip_address)['country_name']] += [g.city(visitor.ip_address)['country_name']]
            count_users[visitor.user] += [visitor.user]
            geolocation[g.city(visitor.ip_address)['country_name']] += [g.city(visitor.ip_address)['country_name'], g.city(visitor.ip_address)['latitude'], g.city(visitor.ip_address)['longitude'] ]
        except (KeyError, AddressNotFoundError) as e:
            try:
                visitor_view.update({(visitor.start_time).strftime("%Y-%m-%d"): [visitor.session_key]})
                country_name.update({g.city(visitor.ip_address)['country_name']: [g.city(visitor.ip_address)['country_name']]})
                geolocation.update({g.city(visitor.ip_address)['country_name']: [g.city(visitor.ip_address)['country_name'], g.city(visitor.ip_address)['latitude'], g.city(visitor.ip_address)['longitude']]})
                count_users.update({visitor.user: [visitor.user]})
            except (KeyError, AddressNotFoundError) as e:
                pass

    return render(request, 'wagalytics/dashboard.html', {
        'pageview': page_view,
        'visitor': visitor_view,
        'count_pageview': Pageview.objects.count(),
        'count_visitor': Visitor.objects.count(),
        'country_name': country_name,
        'count_users': count_users,
        'geolocation': geolocation,
    })
