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
<<<<<<< HEAD
                msg = 'Credenciais Inválidas'
        else:
            msg = 'Erro na validação do Formuário'
=======
                msg = 'Suas credenciais são inválidas'
        else:
            msg = 'Erro ao validar esse campo'
>>>>>>> 81036d86314ea403db0db3345483094056219b2e

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

<<<<<<< HEAD
            msg = 'Usuário criado com sucesso - Por favor <a href="/login">Entre aqui</a>.'
=======
            msg = 'Usuário criado com sucesso - por favor <a href="/login">entre Aqui!</a>.'
>>>>>>> 81036d86314ea403db0db3345483094056219b2e
            success = True

            # return redirect("/login/")

        else:
<<<<<<< HEAD
            msg = 'O formulário não é válido'

=======
            msg = 'Formulário preenchido de forma invalida'
>>>>>>> 81036d86314ea403db0db3345483094056219b2e
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
