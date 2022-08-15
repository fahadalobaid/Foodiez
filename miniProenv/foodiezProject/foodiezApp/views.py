from django.shortcuts import render
from .forms import RegisterForm

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save(commit = False)
            user.set_password(user.password)
          

