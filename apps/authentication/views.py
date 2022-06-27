# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Suas credenciais são inválidas'
        else:
            msg = 'Erro ao validar esse campo'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("Username")
            raw_password = form.cleaned_data.get("Password")
            user = authenticate(username=username, password=raw_password)

            msg = 'Usuário criado com sucesso - por favor <a href="/login">entre Aqui!</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Formulário preenchido de forma invalida'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
