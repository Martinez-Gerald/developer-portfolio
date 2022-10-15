from django.urls import path
from . import views

app_name='devPortfolio'
urlpatterns = [
    path('projects/', views.project_index, name="project_index"),
    path('resume/', views.resume, name="resume"),
]
