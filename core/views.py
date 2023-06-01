import json
from http import HTTPStatus

from django.contrib import messages
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

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
    repo = models.Repo.objects.last()
    registro_versoes = models.RegistroDeVersoes.objects.filter(id_repo=repo.id + 1)
    lgpds = models.LGPD.objects.filter(id_repo=repo.id + 1)
    tabelas = models.Tabelas.objects.filter(id_repo=repo.id + 1)
    abas = models.Abas.objects.filter(id_repo=repo.id + 1)
    querys = models.Querys.objects.filter(id_repo=repo.id + 1)
    context = {}
    data = {}
    user = request.user

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            obj = get_object_or_404(models.Repo, pk=instance.id)
            obj = model_to_dict(obj)
            obj["user_id"] = user.id
            data = json.dumps(
                obj=obj,
                indent=4,
                sort_keys=True
            )

            return JsonResponse(
                data=data,
                safe=False,
                status=HTTPStatus.CREATED
            )

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


def registro_versoes_create(request):
    form = forms.RegistroDeVersoesForm(request.POST or None)
    repo = models.Repo.objects.last()
    data = {}

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)
            instance.id_repo = repo
            instance.save()
            obj = get_object_or_404(models.RegistroDeVersoes, pk=instance.id)
            obj = model_to_dict(obj)
            obj["responsavel"] = models.Responsavel.objects.get(id=obj["responsavel"])
            nome = obj["responsavel"].codigo +' '+ obj["responsavel"].nome
            obj["responsavel"] = nome
            data = json.dumps(
                obj=obj,
                indent=4,
                sort_keys=True
            )

            return JsonResponse(
                data=data,
                safe=False,
                status=HTTPStatus.CREATED
            )


def lgpd_create(request):
    form = forms.LGPDForm(request.POST or None)
    repo = models.Repo.objects.last()
    data = {}

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)
            instance.id_repo = repo
            instance.save()
            obj = get_object_or_404(models.LGPD, pk=instance.id)
            obj = model_to_dict(obj)
            data = json.dumps(
                obj=obj,
                indent=4,
                sort_keys=True
            )

            return JsonResponse(
                data=data,
                safe=False,
                status=HTTPStatus.CREATED
            )


def tabelas_create(request):
    form = forms.TabelasForm(request.POST or None)
    repo = models.Repo.objects.last()
    data = {}

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)
            instance.id_repo = repo
            instance.save()
            obj = get_object_or_404(models.Tabelas, pk=instance.id)
            obj = model_to_dict(obj)
            obj["origem_dados"] = models.TipoOrigemDados.objects.get(id=obj["origem_dados"])
            nome = obj["origem_dados"].nome
            obj["origem_dados"] = nome
            data = json.dumps(
                obj=obj,
                indent=4,
                sort_keys=True
            )

            return JsonResponse(
                data=data,
                safe=False,
                status=HTTPStatus.CREATED
            )


def abas_create(request):
    form = forms.AbasForm(request.POST or None)
    repo = models.Repo.objects.last()
    data = {}

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)
            instance.id_repo = repo
            instance.save()
            obj = get_object_or_404(models.Abas, pk=instance.id)
            obj = model_to_dict(obj)
            data = json.dumps(
                obj=obj,
                indent=4,
                sort_keys=True
            )

            return JsonResponse(
                data=data,
                safe=False,
                status=HTTPStatus.CREATED
            )


def querys_create(request):
    form = forms.QuerysForm(request.POST or None)
    repo = models.Repo.objects.last()
    data = {}

    if request.method == "POST":

        if form.is_valid():
            instance = form.save(commit=False)
            instance.id_repo = repo
            instance.save()
            obj = get_object_or_404(models.Querys, pk=instance.id)
            obj = model_to_dict(obj)
            data = json.dumps(
                obj=obj,
                indent=4,
                sort_keys=True
            )

            return JsonResponse(
                data=data,
                safe=False,
                status=HTTPStatus.CREATED
            )
