from django.urls import path

from . import views

app_name = "sorteo_app"

urlpatterns = [
    path(
        'sorteo',
        views.SorteoView.as_view(),
        name="sorteo"
    ),
]
