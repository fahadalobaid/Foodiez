from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField( User,on_delete=models.CASCADE,)
  
    image = models.ImageField( blank=True, null=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    Bio = models.TextField(max_length=180)
    email = models.EmailField(max_length = 254)

    def __str__(self):
        return self.user.username


class Ingredient(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name




class Categorie(models.Model):
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to = 'foodiezApp/images', blank=True, null=True)
    ingredients = models.ManyToManyField( Ingredient,related_name="ingredients")
    discription = models.TextField (default="Write your delicious recipe")
    categories =  models.ForeignKey( Categorie,on_delete=models.CASCADE,related_name="categories" )

    def __str__(self):
        return self.name





