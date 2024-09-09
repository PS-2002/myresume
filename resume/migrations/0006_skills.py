# Generated by Django 5.0.3 on 2024-07-25 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_details_objective'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language1', models.CharField(max_length=20)),
                ('language2', models.CharField(max_length=20)),
                ('web_framework1', models.CharField(max_length=20)),
                ('web_framework2', models.CharField(max_length=20)),
                ('frontend_technologies', models.CharField(max_length=20)),
                ('dbms1', models.CharField(max_length=20)),
                ('dbms2', models.CharField(max_length=20)),
                ('cloud_service', models.CharField(max_length=100)),
            ],
        ),
    ]
