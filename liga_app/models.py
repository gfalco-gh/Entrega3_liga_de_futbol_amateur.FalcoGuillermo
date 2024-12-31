from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class League(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    founded_date = models.DateField()
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    points = models.PositiveIntegerField(default=0)  # Puntos para posiciones
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)
    escudo = models.ImageField(upload_to='equipos_escudos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    goals = models.PositiveIntegerField(default=0)  # Goleadores
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.name} {self.apellido}'


class Match(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.home_score}-{self.away_score})"

class Estadistica(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    goals = models.PositiveIntegerField(default=0)
    asistencias = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Estadísticas de {self.player}'

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)