from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from . import models
from . import forms


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


def repos(request):
    form = forms.RepoForm(request.POST or None)
    registro_versoes_form = forms.RegistroDeVersoesForm(request.POST or None)
    lgpd_form = forms.LGPDForm(request.POST or None)
    tabelas_form = forms.TabelasForm(request.POST or None)
    abas_form = forms.AbasForm(request.POST or None)
    query_form = forms.QuerysForm(request.POST or None)
    repos = models.Repo.objects.all()
    registro_versoes = models.RegistroDeVersoes.objects.all()
    lgpds = models.LGPD.objects.all()
    tabelas = models.Tabelas.objects.all()
    abas = models.Abas.objects.all()
    querys = models.Querys.objects.all()
    context = {}
    user = request.user

    if request.method == "POST":

        if form.is_valid():
            form.save()

            return redirect("core:repos")

    elif registro_versoes_form.is_valid():
            registro_versoes_form.save()

            return redirect("core:repos")

    else:
        form = forms.RepoForm(request.POST or None)
        registro_versoes_form = forms.RegistroDeVersoesForm(request.POST or None)
        lgpd_form = forms.LGPDForm(request.POST or None)
        tabelas_form = forms.TabelasForm(request.POST or None)
        abas_form = forms.AbasForm(request.POST or None)
        query_form = forms.QuerysForm(request.POST or None)
    
    context["form"] = form
    context["registro_versoes_form"] = registro_versoes_form
    context["registro_versoes"] = registro_versoes
    context["lgpd_form"] = lgpd_form
    context["tabelas_form"] = tabelas_form
    context["abas_form"] = abas_form
    context["query_form"] = query_form
    context["repos"] = repos
    context["lgpds"] = lgpds
    context["tabelas"] = tabelas
    context["abas"] = abas
    context["querys"] = querys
    context["user"] = user

    return render(
        request=request,
        template_name="core/repos.html",
        context=context
    )
