from django.urls import path

from . import views

app_name = "home_app"

urlpatterns = [
    path(
        '',
        views.HomeView.as_view(),
        name="home"
    ),
    path(
        'estadisticas',
        views.EstadisticasView.as_view(),
        name="estadisticas"
    ),
]
