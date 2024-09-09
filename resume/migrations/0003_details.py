# Generated by Django 5.0.3 on 2024-07-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_experience_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=15)),
                ('linkedin_url', models.CharField(max_length=200)),
                ('github_url', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/%y/%m/%d')),
            ],
        ),
    ]