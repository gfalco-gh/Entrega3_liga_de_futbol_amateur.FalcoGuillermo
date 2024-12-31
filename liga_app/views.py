from django.shortcuts import render, redirect, get_object_or_404
from .models import League, Team, Player, Match, BlogPost
from .forms import LeagueForm, TeamForm, PlayerForm, MatchForm, TeamSearchForm, RegistroForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Team
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
#from django.contrib.auth.decorators import login_required

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

def home(request):
    return render(request, 'liga_app/home.html')

def about(request):
    return render(request, 'liga_app/about.html')

class BlogListView(ListView):
    model = BlogPost
    template_name = 'liga_app/blog_list.html'
    context_object_name = 'blogs'

def post_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

class EquipoListView(ListView):
    model = Team
    template_name = 'liga_app/equipo_list.html'
    context_object_name = 'equipos'

class EquipoCreateView(CreateView):
    model = Team
    template_name = 'liga_app/equipo_form.html'
    fields = ['nombre', 'ciudad', 'escudo', 'fundado_en']
    success_url = reverse_lazy('equipo_list')

class EquipoUpdateView(UpdateView):
    model = Team
    template_name = 'liga_app/equipo_form.html'
    fields = ['nombre', 'ciudad', 'escudo', 'fundado_en']
    success_url = reverse_lazy('equipo_list')

class EquipoDeleteView(DeleteView):
    model = Team
    template_name = 'liga_app/equipo_confirm_delete.html'
    success_url = reverse_lazy('equipo_list')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Cambia 'home' por la ruta de tu vista principal
    else:
        form = AuthenticationForm()
    return render(request, 'liga_app/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después del registro
    else:
        form = UserCreationForm()
    return render(request, 'liga_app/signup.html', {'form': form})

#Este código muestra un formulario para crear un nuevo usuario, guarda los datos cuando el formulario es válido 
# y redirige al usuario a la página de inicio de sesión.

def profile(request):
    # Lógica para mostrar el perfil
    return render(request, 'liga_app/profile.html')

def signup_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Cambia esto al nombre correcto de tu vista de inicio de sesión
    else:
        form = RegistroForm()
    return render(request, 'liga_app/sign_up.html', {'form': form})