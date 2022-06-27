from django import forms
from django.utils.translation import ugettext_lazy as _

from apps.home.models import Pessoa


class PcdForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(PcdForm, self).__init__(*args, **kwargs)
        self.fields['deficiencia'].localize = True

    class Meta:
        model = Pessoa
        fields = ('nome', 
                'informacoes_adicionais', )
        widgets = {
            # 'nome_secretaria': forms.TextInput(attrs={'class': 'form-control'}),
            'nome': forms.RadioSelect(attrs={'class': 'form-control'}),
            'informacoes_adicionais': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            # 'nome_secretaria': _('Nome da Secretaria'),
            'nome': _(''),
            'informacoes_adicionais': _('Informações Adicionais'),
        }

    def save(self, commit=True):
        instance = super(PcdForm, self).save(commit=False)
        instance.criado_por = self.request.user
        if commit:
            instance.save()
        return instance
