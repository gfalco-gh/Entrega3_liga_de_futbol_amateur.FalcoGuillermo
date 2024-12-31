"""
URL configuration for liga_de_futbol_amateur project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from liga_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('liga_app.urls')),  # Enlazar las URLs de la app
    path('messages/', include('messaging.urls')),  # Mensajería
    path('', views.index, name='index'),  # Página de inicio
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Vista de login
    path('signup/', views.signup_view, name='signup'),  # Vista de signup personalizada
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Vista de logout
    path('profile/', views.profile, name='profile'),  # Página de perfil
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]

# Sirve archivos media durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
