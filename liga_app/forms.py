from django import forms
from .models import League, Team, Player, Match
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name', 'region']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'founded_date', 'league']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'founded_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'league': forms.Select(attrs={'class': 'form-control'}),
        }

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'team', 'goals', 'yellow_cards', 'red_cards']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'team': forms.Select(attrs={'class': 'form-control'}),
            'goals': forms.NumberInput(attrs={'class': 'form-control'}),
            'yellow_cards': forms.NumberInput(attrs={'class': 'form-control'}),
            'red_cards': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'home_team', 'away_team', 'home_score', 'away_score']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'home_team': forms.Select(attrs={'class': 'form-control'}),
            'away_team': forms.Select(attrs={'class': 'form-control'}),
            'home_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'away_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class TeamSearchForm(forms.Form):
    query = forms.CharField(label="Buscar equipo", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']