# Generated by Django 4.1 on 2022-08-15 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("foodiezApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipes",
            old_name="Categ",
            new_name="categories",
        ),
        migrations.RenameField(
            model_name="recipes",
            old_name="Ingre",
            new_name="ingredients",
        ),
    ]