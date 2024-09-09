from django.urls import path
from .views import owner_login, owner_logout, edit_project, add_experience, add_certificate

urlpatterns = [
    path('login/', owner_login, name='login'),
    path('logout/', owner_logout, name = 'logout'),
    path('edit_project/', edit_project, name = 'edit_project'),
    path('add_experience/', add_experience, name = 'add_experience'),
    path('add_certificate/', add_certificate, name = 'add_certificate')
]