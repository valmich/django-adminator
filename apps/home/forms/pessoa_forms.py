# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from apps.home.models import Pessoa

class PessoaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            instance = kwargs.pop('instance')
            instance = Pessoa.objects.get(pk=instance.pk)
            super(PessoaForm, self).__init__(
                instance=instance, *args, **kwargs)
        else:
            super(PessoaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pessoa
        fields = ('cpf', 'rg', 'nascimento', )

        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'rg': forms.TextInput(attrs={'class': 'form-control'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control datepicker'}),
        }
        labels = {
            'cpf': _('CPF'),
            'rg': _('RG'),
            'nascimento': _('Nascimento'),
        }
