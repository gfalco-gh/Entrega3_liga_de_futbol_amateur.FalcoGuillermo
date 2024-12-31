from django.urls import path
from .views import MensajeListView

urlpatterns = [
    path('', MensajeListView.as_view(), name='mensaje_list'),
]
