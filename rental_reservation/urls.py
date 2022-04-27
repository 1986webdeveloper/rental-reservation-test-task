# -*- coding: utf-8 -*-

"""
    Used to manage all the URL's related to homepage
"""
from django.urls import path
from rental_reservation.views import (
    HomePageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
]
