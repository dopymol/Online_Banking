from .models import Ways

def menu_links(request):
    links = Ways.objects.all()
    return dict(links=links)