# Generated by Django 4.1 on 2022-08-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodiezApp", "0003_alter_recipe_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/foodiezApp/images "
            ),
        ),
    ]
