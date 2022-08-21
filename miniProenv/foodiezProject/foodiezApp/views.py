from multiprocessing import context
from django.shortcuts import render ,redirect
from django.contrib.auth import login ,authenticate ,logout
from .forms import RegisterForm,LoginForm,RecipeForm,IngredientForm,CategoriesForm
from .models import Recipe

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save()
            user.set_password(user.password)
            user.save()


            login(request,user)

            return redirect('recipes')



    context = {"form":form,}
          
    return render(request,'register.html',context)


def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticate_user = authenticate(username=username, password=password)
            login(request,authenticate_user)
            return redirect('recipes')

    
    context = {"form":form}
    

    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect ("login")



def recipes_details(request,recipes_id):
    recipes = Recipe.objects.get(id=recipes_id)

    context ={
        "recipes":recipes


    }
    return render(request,"Recipes_details.html",context)



def recipe_list(request):
    recipes= Recipe.objects.all()
    context={
        "recipes":recipes}

    return render(request,"Recipes.html",context)



def create_recipe(request):
    if not request.user.is_authenticated:
        return redirect("login")
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {

        "form":form,
    }
    return render(request,"create_recipes.html",context)




def update_recipe(request,recipe_id):
    if not request.user.is_authenticated:
        return redirect("login")
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForm(instance=recipe)
    if request.method == "POST":
        form = RecipeForm(request.POST,instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {

        "form":form,
        "recipe":recipe,
    }

    return render(request,"update_recipes.html",context)




def delete(request,recipe_id):
    if not request.user.is_authenticated:
        return redirect("login")
    recipe = Recipe.objects.get(id =recipe_id)
    recipe.delete()
    return redirect('recipes')



def create_ingre(request):
    if not request.user.is_authenticated:
        return redirect("login")
    form = IngredientForm()
    if request.method == "POST":
        form = IngredientForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {

        "form":form,
    }
    return render(request,"create_ingredient.html",context)



def create_Categorie(request):
    if not request.user.is_authenticated:
        return redirect("login")
    form = CategoriesForm()
    if request.method == "POST":
        form = CategoriesForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {

        "form":form,
    }
    return render(request,"create_categories.html",context)






