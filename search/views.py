from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from blog.models import Single_postPage
from wagtail.search.models import Query


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    # Search
    if search_query:
        search_results = Single_postPage.objects.live().search(search_query)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    else:
        search_results = Single_postPage.objects.none()

    # Pagination
    paginator = Paginator(search_results, 1)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
