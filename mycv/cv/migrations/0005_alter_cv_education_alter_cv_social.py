# Generated by Django 4.2.5 on 2023-09-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cv", "0004_cv_education_cv_social"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cv",
            name="education",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="cv",
            name="social",
            field=models.TextField(default=""),
        ),
    ]
