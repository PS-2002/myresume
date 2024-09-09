from django import forms
from resume.models import Experience, Details, Skills, Projects, Certificates

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) 


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('role', 'company_name', 'certificates', 'task')

class DetailsForm(forms.ModelForm):

    class Meta:
        model = Details
        fields = ('name', 'role', 
                  'email', 'phone', 
                  'linkedin_url', 'github_url',
                  'image', 'objective')

class SkillsForm(forms.ModelForm):

    class Meta:
        model = Skills
        fields = ('language1', 'language2', 
                 'web_framework1', 'web_framework2',
                 'frontend_technologies', 'dbms1',
                 'dbms2', 'cloud_service',
                 'version_control', 'other')
        

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ('title', 'skills_used', 'description', 'link')


class CertificatesForm(forms.ModelForm):

    class Meta:
        model = Certificates
        fields = ('name', 'certificate_img')


        


