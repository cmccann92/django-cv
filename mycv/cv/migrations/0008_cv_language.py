# Generated by Django 4.2.5 on 2023-10-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cv", "0007_remove_cv_social_cv_github_link_cv_linkedin_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="cv",
            name="language",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]