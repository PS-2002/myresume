# Generated by Django 5.0.3 on 2024-07-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_skills_version_control'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_img', models.ImageField(upload_to='images/%y/%m/%d')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
