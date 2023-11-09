from django.db import models


class CV(models.Model):
    language = models.CharField(blank = True, max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    skills = models.TextField()
    about_me = models.TextField()
    education = models.TextField(default="")
    work_experience = models.TextField()
    linkedin_link = models.URLField(blank = True)
    github_link = models.URLField(blank = True)
    picture = models.ImageField(upload_to="pictures/", null=True, blank=True)


