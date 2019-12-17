from django.shortcuts import render
from .itunes_api import iTunesApi
import json

def results(request):
    if request.method == "POST":
        search_term = request.POST.get('search_term')
        search_term_results = iTunesApi().search_itunes_api("NL", search_term)['results']
        return render(request, "itunes_api/index.html", {'results': search_term_results})

    return render(request, "itunes_api/index.html", {})