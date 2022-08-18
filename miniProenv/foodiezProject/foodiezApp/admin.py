from django.contrib import admin
from .models import Categorie,Ingredient,Recipe,Profile

admin.site.register(Profile)
admin.site.register(Categorie)
admin.site.register(Ingredient)
admin.site.register(Recipe)

