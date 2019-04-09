from django.shortcuts import render


def handler404(request, exception):
    return render(request, "merken/404.html", status=404)


def handler500(request):
    return render(request, "merken/500.html", status=500)
