from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField( User,on_delete=models.CASCADE,)
  
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    Bio = models.TextField(max_length=180)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.user.username


class Ingredients(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name




class Categories(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Recipes(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,)
    ingredients = models.ManyToManyField( Ingredients,related_name="ingredients")
    discription = models.TextField (default="Write your delicious recipe")
    categories =  models.ForeignKey( Categories,on_delete=models.CASCADE,related_name="categories" )

    def __str__(self):
        return self.name





