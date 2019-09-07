from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
import datetime

from wagtail.core.models import Page
from wagtail.search.models import Query
from django.shortcuts import redirect, render
from django.utils import timezone


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
    initial_start_date = (timezone.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")

    return render(request, 'wagalytics/dashboard.html', {
        'ga_view_id': "Hello World",
        'initial_start_date': initial_start_date,
    })
