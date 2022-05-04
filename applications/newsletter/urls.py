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
        'save-newsletter',
        views.newsletter,
        name="save-newsletter"
    ),
    path(
        'estadisticas',
        views.EstadisticasView.as_view(),
        name="estadisticas"
    ),
    path(
        'testimonios',
        views.TestimoniosView.as_view(),
        name="testimonios"
    ),
]
