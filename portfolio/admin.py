from django.contrib import admin
from .models import Project, GithubProject

admin.site.register(Project)
admin.site.register(GithubProject)
