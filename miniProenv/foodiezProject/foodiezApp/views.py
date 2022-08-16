from multiprocessing import context
from django.shortcuts import render ,redirect
from django.contrib.auth import login ,authenticate
from .forms import RegisterForm,LoginForm

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            user = form.save()
            user.set_password(user.password)
            user.save()


            login(request,user)

            return redirect('home')



    context = {"form":form,}
          
    return render(request,'register.html',context)


def Login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            authenticate_user = authenticate(username=username, password=password)
            login(request,authenticate_user)
            return redirect('home')

    
    context = {"form":form,}

    return render(request,'login.html',context)

