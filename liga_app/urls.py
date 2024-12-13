from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-league/', views.create_league, name='create_league'),
    path('create-team/', views.create_team, name='create_team'),
    path('create-player/', views.create_player, name='create_player'),
    path('create-match/', views.create_match, name='create_match'),
    path('search-teams/', views.search_teams, name='search_teams'),
]
