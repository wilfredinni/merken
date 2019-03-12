from django.http import HttpResponse


def blog(request):
    return HttpResponse("Blog Page")


def article(request):
    return HttpResponse("Article page")


def article_by_tag(request):
    return HttpResponse("Articles by tags")
