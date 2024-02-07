from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.project_list),
    path("filter/", views.filter_projects, name= 'filter_projects'),
    path("resume/", views.generate_resume, name='generate_resume'),

]
