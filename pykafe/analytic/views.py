from django.shortcuts import render
from tracking.models import Visitor, Pageview
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError


def dashboard(request):
    dict_view = {}
    visitor_view = {}
    country_name = {}
    count_users = {}
    g = GeoIP2()
    for page in Pageview.objects.all():
        for filterpage in Pageview.objects.filter(url=page.url).distinct():
            dict_view.update({ filterpage.url: Pageview.objects.filter(url=page.url).count()})
    for visitor in Visitor.objects.all():
        try:
            visitor_view[(visitor.start_time).strftime("%Y-%m-%d")] += [visitor.session_key]
        except KeyError:
            visitor_view.update({(visitor.start_time).strftime("%Y-%m-%d"): [visitor.session_key]})
        try:
            country_name[g.city(visitor.ip_address)['country_name']] += [g.city(visitor.ip_address)['country_name']]
        except (KeyError, AddressNotFoundError) as e:
            try:
                country_name.update({g.city(visitor.ip_address)['country_name']: [g.city(visitor.ip_address)['country_name']]})
            except (KeyError, AddressNotFoundError) as e:
                pass
        try:
            count_users[visitor.user] += [visitor.user]
        except KeyError:
             count_users.update({visitor.user: [visitor.user]})

    return render(request, 'wagalytics/dashboard.html', {
        'pageview': dict_view,
        'visitor': visitor_view,
        'count_pageview': Pageview.objects.count(),
        'count_visitor': Visitor.objects.count(),
        'country_name': country_name,
        'count_users': count_users,
    })
