# Generated by Django 4.2.5 on 2023-09-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cv", "0003_cv_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="cv",
            name="education",
            field=models.CharField(default=""),
        ),
        migrations.AddField(
            model_name="cv",
            name="social",
            field=models.CharField(default=""),
        ),
    ]
