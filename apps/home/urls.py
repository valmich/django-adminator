from django.urls import path, re_path
from apps.home.views import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),


    # Matches any html file
    re_path(r'cadastro/', views.cadastro, name='cadastro'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
