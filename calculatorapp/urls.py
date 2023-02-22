from django.urls import path
from .views import *

urlpatterns=[

    path("freak",freak),
    path("calculator/",calculator)


    ]