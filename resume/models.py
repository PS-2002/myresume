from django.db import models
from django.utils.text import slugify
# Create your models here.
class Experience(models.Model):

    role = models.CharField(max_length=100)
    task = models.TextField(null= True)
    company_name = models.CharField(max_length=100)
    certificates = models.ImageField(upload_to='images/%y/%m/%d')
    slug = models.SlugField(max_length=200, blank=True)

    def __str__(self):
        return self.role

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.role)
        super().save(*args, **kwargs)

class Details(models.Model):

    name = models.CharField(max_length=20)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    linkedin_url = models.CharField(max_length=200)
    github_url = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    slug = models.SlugField(max_length=200, blank=True)
    objective = models.TextField(null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
class Skills(models.Model):

    language1 = models.CharField(max_length=20)
    language2 = models.CharField(max_length=20)
    web_framework1 = models.CharField(max_length=20)
    web_framework2 = models.CharField(max_length=20)
    frontend_technologies = models.CharField(max_length=20)
    dbms1 = models.CharField(max_length=20)
    dbms2 = models.CharField(max_length=20)
    cloud_service = models.CharField(max_length=20)
    version_control = models.CharField(max_length=20, null=True)
    other = models.CharField(max_length=100, null=True)


class Projects(models.Model):

    title = models.CharField(max_length=20, null=True)
    skills_used = models.CharField(max_length=20, null=True)
    description = models.TextField(null=True)
    link = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title
    
class Certificates(models.Model):

    certificate_img = models.ImageField(upload_to='images/%y/%m/%d')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
