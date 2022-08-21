"""foodiezProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodiezApp.views import register_user,login_user,recipes_details,recipe_list,create_recipe,update_recipe,delete,create_ingre
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", register_user,name="register"),
    path("login/", login_user,name="login"),
    path("home/", recipe_list,name="recipes"),
    path("recipes/<int:recipes_id>/", recipes_details,name="recipes"),
    path("create/",create_recipe ,name="recipe_form"),
    path("create-Ingredients/",create_ingre,name="ingredients_form"),
    path("update/<int:recipe_id>",update_recipe ,name="recipe_update_form"),
    path("delete/<int:recipe_id>",delete,name="recipe_delete"),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

