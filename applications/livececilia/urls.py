from django.urls import path

from . import views

app_name = "livececilia_app"

urlpatterns = [
    path(
        'livececilia',
        views.LiveCeciliaView.as_view(),
        name="livececilia"
    ),
]
