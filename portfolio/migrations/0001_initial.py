# Generated by Django 5.1.4 on 2024-12-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GithubProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('github_name', models.CharField(max_length=100)),
                ('stars', models.IntegerField()),
                ('forks', models.IntegerField()),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='projects/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='projects/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
