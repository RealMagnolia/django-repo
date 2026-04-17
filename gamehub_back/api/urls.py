from django.urls import path
from . import views 
from django.http import HttpResponse

def api_root(request):
    return HttpResponse("OK")

urlpatterns = [
    path('games/', views.games_list),
    path('genres/', views.genres_list.as_view())
]