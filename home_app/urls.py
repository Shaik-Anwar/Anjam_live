from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ece_projects/', views.ece, name="ece"),
    path('cse_projects/', views.cse, name="cse"),
    path('eee_projects/', views.eee, name="eee"),
]