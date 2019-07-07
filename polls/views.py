from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect

# def index(request):
#     c = request.POST["content"]
#     new = c.title()
#     newup = c.upper()
#     return render(request, 'convert.html', {"new":new, "newup":newup})

def index(request):
    c =request.POST.get("content", "gjhd")
    new = c.title()
    count = c.count(" ")
    return render(request, 'convert.html', {"new":new, "count":count}) 

def small(request):
    if request.GET.get('allsmall'):
        c = request.POST.get("content", "gjhd")
        newsmall = c.lower()
    return render_to_response(request, 'convert.html', {'newsmall': newsmall})