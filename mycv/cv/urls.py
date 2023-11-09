from django.urls import path, include
from .views import english_cv_view, german_cv_view


urlpatterns = [
    path("", english_cv_view, name="cv_view"),
    path("german/", german_cv_view, name="cv_view_german")
]


