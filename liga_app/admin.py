from django.contrib import admin
from .models import BlogPost, Team, Player, Estadistica

# Register your models here.

admin.site.register(BlogPost)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Estadistica)
