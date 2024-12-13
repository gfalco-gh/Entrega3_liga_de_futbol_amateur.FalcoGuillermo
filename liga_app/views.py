from django.shortcuts import render, get_object_or_404, redirect
from .models import League, Team, Player, Match
from .forms import LeagueForm, TeamForm, PlayerForm, MatchForm, TeamSearchForm

# Create your views here.


# Vista para la página principal
def index(request):
    return render(request, 'liga_app/index.html')

# Crear Liga
def create_league(request):
    if request.method == 'POST':
        form = LeagueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LeagueForm()
    return render(request, 'liga_app/form.html', {'form': form, 'title': 'Registrar Liga'})

# Crear Equipo
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TeamForm()
    return render(request, 'liga_app/form.html', {'form': form, 'title': 'Registrar Equipo'})

# Crear Jugador
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PlayerForm()
    return render(request, 'liga_app/form.html', {'form': form, 'title': 'Registrar Jugador'})

# Registrar Partido
def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MatchForm()
    return render(request, 'liga_app/form.html', {'form': form, 'title': 'Registrar Partido'})

# Buscar Equipos
def search_teams(request):
    form = TeamSearchForm(request.GET or None)
    teams = []
    if form.is_valid():
        query = form.cleaned_data['query']
        teams = Team.objects.filter(name__icontains=query)
    return render(request, 'liga_app/search.html', {'form': form, 'teams': teams})

