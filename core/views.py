from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    template_name = 'user/loginRegister.html'
    form = AuthenticationForm(request, data=request.POST)
    title = "Log in"
    context = {}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(
            username=username, 
            password=password
        )
        login(request, user)

        return redirect("core:index")
    else:
        messages.error(request,"Invalid username or password.")

    context["title"] = title
    context["form"] = form

    return render(request, template_name, context)


@login_required
def user_logout(request):
    logout(request)

    return redirect('login')


@login_required
def index(request):
    template_name = 'core/index.html'

    return render(request, template_name)