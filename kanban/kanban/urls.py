from django.urls import path

from . import views

app_name = "kanban"

#views.indexに繋がる
urlpatterns = [
    path("", views.index, name="index"),
]

