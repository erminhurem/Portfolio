from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class GithubProject(models.Model):
    title = models.CharField(max_length=100)
    github_name = models.CharField(max_length=100)
    stars = models.IntegerField()
    forks = models.IntegerField()
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


