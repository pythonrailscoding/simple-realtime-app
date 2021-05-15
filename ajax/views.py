from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from .models import Profile

def index(request):
    return render(request, 'index.html', {})

def getResponse(request):
    entries = Profile.objects.all().order_by('-id')
    return JsonResponse({'entries':list(entries.values())})

def create(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
            new_field = Profile(name=name)
            new_field.save()
        else:
            name = False
    return render(request, 'create.html', {})
