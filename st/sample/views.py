from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect


def index(reqest):
    return HttpResponse("SAMPLE")


def categories(reqest, catid):
    if reqest.GET:
        print(reqest.GET)

    else:
        print('nihuya')
    return HttpResponse(f"<h1>BIG SAMPLE</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>BIG SAMPLE</h1><p>{year}</p>")


def pageNotFound(request, exception):
    print(request.GET)
    return HttpResponseNotFound("<h1>Brother you confused something</h1>")

def apihelp(request):
    return HttpResponse('<h1>API DOCUMENTATION HELP</h1>')
