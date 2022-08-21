from django import forms
from django.contrib.auth import get_user_model
from .models import Recipe , Ingredient ,Categorie


User = get_user_model()



class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email',]
        widgets = {"password" : forms.PasswordInput(),}


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, )
    widgets={"password" : forms.PasswordInput(),}



class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name','image','ingredients','discription','categories']


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name']

