from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import UrlForm
from .models import Url
from app.functions import generate_url


ERROR_404 = "<h2>Ошибка 404. Нет такой страницы</h2>"

def index(request):
    form = UrlForm()
    if request.method == "POST":
        long_url = request.POST["url"]
        domain = get_current_site(request).domain
        short_url, img = generate_url(domain, long_url)
        return render(request, "app/index.html",
        {
            'url': short_url,
            'form': form,
            'img': img
        })
    else:
        return render(request, "app/index.html", {'form': form})


def redirect(request, path):
    if Url.objects.filter(short_path=path).exists():
        url = Url.objects.get(short_path=path)
        redirect_path = url.long_url
        return HttpResponsePermanentRedirect(redirect_path)
    else:
        return HttpResponseNotFound(ERROR_404)


def api(request):
    if request.method == "GET":
        if 'url' in request.GET:
            long_url = request.GET["url"]
            domain = get_current_site(request).domain
            full_url, img = generate_url(domain, long_url)
            return HttpResponse(full_url)
        else:
            site_url = ''.join(['http://', get_current_site(request).domain])
            return render(request, "app/api.html", {'site_url': site_url})
    else:
        return HttpResponseNotFound(ERROR_404)
