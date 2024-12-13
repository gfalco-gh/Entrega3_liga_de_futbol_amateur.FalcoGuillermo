from django.db import models

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
        return self.name

class Match(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} ({self.home_score}-{self.away_score})"

