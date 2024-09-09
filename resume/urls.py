from django.urls import path
from .views import resume, experience, education, skills, projects, certificates


urlpatterns = [
    path('', resume, name='resume'),
    path('experience/', experience, name='experience'),
    path('education/', education, name= 'education'),
    path('skills/', skills, name='skills'),
    path('projects/', projects, name='projects'),
    path('certificates/', certificates, name='certificates')
]