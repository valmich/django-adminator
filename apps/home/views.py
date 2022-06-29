from email.mime import base
from time import strftime
from django import template
import django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.home.models import Pessoa, Cid, LocalAvaliacao, ResumoIncapacidade, Participacao
from apps.home.models.pcd import Pcd
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from django.shortcuts import render

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}

    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/forms.html' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
