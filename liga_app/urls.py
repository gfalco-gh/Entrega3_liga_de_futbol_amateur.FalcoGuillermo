from django.urls import path
from . import views
from .views import about, home, BlogListView, EquipoListView, EquipoCreateView, EquipoUpdateView, EquipoDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('create-league/', views.create_league, name='create_league'),
    path('create-team/', views.create_team, name='create_team'),
    path('create-player/', views.create_player, name='create_player'),
    path('create-match/', views.create_match, name='create_match'),
    path('search-teams/', views.search_teams, name='search_teams'),
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('', home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]

urlpatterns += [
    path('about/', about, name='about'),
]

urlpatterns += [
    path('pages/', BlogListView.as_view(), name='blog_list'),
]

urlpatterns += [
    path('equipos/', EquipoListView.as_view(), name='equipo_list'),
    path('equipos/nuevo/', EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/<int:pk>/editar/', EquipoUpdateView.as_view(), name='equipo_update'),
    path('equipos/<int:pk>/eliminar/', EquipoDeleteView.as_view(), name='equipo_delete'),
]