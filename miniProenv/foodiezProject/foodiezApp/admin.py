from django.contrib import admin
from .models import Categories,Ingredients,Recipes,Profile

admin.site.register(Profile)
admin.site.register(Categories)
admin.site.register(Ingredients)
admin.site.register(Recipes)

