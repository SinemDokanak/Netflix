from django.shortcuts import render
from .models import *
from django.db.models import Q
from user.models import *
# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, id):
    profile = Profiles.objects.get(id = id)
    filmler = Movie.objects.all()
    profiller = Profiles.objects.filter(owner = request.user)
    
    context = {
        'filmler':filmler,
        'profile':profile,
        'profiller':profiller
    }
    # print(context['filmler'])
    return render(request, 'browse-index.html', context)

def search(request):
    search = request.GET.get('search')
    filmler = Movie.objects.filter(
        Q(isim__icontains = search) |
        Q(kategori__isim__icontains = search)
    )
    context = {
        'search':search,
        'filmler':filmler
    }
    return render(request, 'search.html', context)