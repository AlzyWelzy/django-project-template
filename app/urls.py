from django.urls import path, re_path
from .views import *

main_site = [
    path("", index, name="index"),
    re_path(r"^.*/$", error_page, name="error_page"),
]

urlpatterns = main_site
