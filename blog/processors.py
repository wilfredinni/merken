from pages.models import Page


def site_name(request):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    # TODO: site_name must come from the database
    context = {"site_name": "Python Cheatsheet"}
    return context


def custom_pages(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return context
