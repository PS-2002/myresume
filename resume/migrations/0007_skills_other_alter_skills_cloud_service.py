# Generated by Django 5.0.3 on 2024-07-25 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='other',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='cloud_service',
            field=models.CharField(max_length=20),
        ),
    ]