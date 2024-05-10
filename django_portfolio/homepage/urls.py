from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("read-me/a-gods-draw", views.agodsdraw, name="agodsdraw"),
    path("read-me/negative-effect", views.negativeeffect, name="negativeeffect")
]