from apps.home.custom_views import CustomCreateView, CustomListView, CustomUpdateView

from apps.home.forms import PessoaForm, EnderecoFormSet, TelefoneFormSet, EmailFormSet, \
    SiteFormSet, BancoFormSet, DocumentoFormSet
from apps.home.models import Pessoa,  Endereco, Telefone, Email, Site, Banco, Documento


class AdicionarPessoaView(CustomCreateView):

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, nome=self.object.nome)

    def get(self, request, form, *args, **kwargs):
        self.object = None

        pessoa_form = PessoaForm(prefix='pessoa_form')

        endereco_form = EnderecoFormSet(prefix='endereco_form')
        endereco_form.can_delete = False

        banco_form = BancoFormSet(prefix='banco_form')
        banco_form.can_delete = False

        documento_form = DocumentoFormSet(prefix='documento_form')
        documento_form.can_delete = False

        telefone_form = TelefoneFormSet(prefix='telefone_form')
        email_form = EmailFormSet(prefix='email_form')
        site_form = SiteFormSet(prefix='site_form')

        formsets = [telefone_form, email_form, site_form]
        for formset in formsets:
            formset.can_delete = False

        return self.render_to_response(self.get_context_data(form=form,
                                                             pessoa_form=pessoa_form,
                                                             endereco_form=endereco_form,
                                                             banco_form=banco_form,
                                                             documento_form=documento_form,
                                                             formsets=formsets))

    def post(self, request, form, *args, **kwargs):
        self.object = None
        extra_forms = []

        endereco_form = EnderecoFormSet(request.POST, prefix='endereco_form')
        banco_form = BancoFormSet(request.POST, prefix='banco_form')
        documento_form = DocumentoFormSet(
            request.POST, prefix='documento_form')

        telefone_form = TelefoneFormSet(request.POST, prefix='telefone_form')
        email_form = EmailFormSet(request.POST, prefix='email_form')
        site_form = SiteFormSet(request.POST, prefix='site_form')

        formsets = [telefone_form, email_form, site_form]

        if form.is_valid():
            self.object = form.save(commit=False)
            pessoa_form = PessoaForm(
                request.POST, prefix='pessoa_form')

            if (all(formset.is_valid() for formset in formsets) and
                pessoa_form.is_valid() and
                endereco_form.is_valid() and
                banco_form.is_valid() and
                documento_form.is_valid() and
                    all(extra_form.is_valid() for extra_form in extra_forms)):

                self.object.save()

            # Salvar informacoes endereco
            endereco_form.instance = self.object
            end = endereco_form.save()
            if len(end):
                self.object.endereco_padrao = end[0]

            # Salvar informacoes bancarias
            banco_form.instance = self.object
            ban = banco_form.save()
            if len(ban):
                self.object.banco_padrao = ban[0]

            # Salvar documentos adicionais
            documento_form.instance = self.object
            documento_form.save()

            # salvar telefone
            telefone_form.instance = self.object
            tel = telefone_form.save()
            if len(tel):
                self.object.telefone_padrao = tel[0]

            # salvar email
            email_form.instance = self.object
            ema = email_form.save()
            if len(ema):
                self.object.email_padrao = ema[0]

            # salvar site
            site_form.instance = self.object
            sit = site_form.save()
            if len(sit):
                self.object.site_padrao = sit[0]


            # salvar objeto criado e pessoa fisica
            self.object.save()
            pessoa_form.instance.pessoa_id = self.object
            pessoa_form.save()

            return self.form_valid(form)

class PessoasListView(CustomListView):

    def __init__(self, *args, **kwargs):
        super(PessoasListView, self).__init__(*args, **kwargs)


class EditarPessoaView(CustomUpdateView):

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, nome_social=self.object.nome_social)

    def get(self, request, form, *args, **kwargs):
        pessoa_form = PessoaForm(
                instance=self.object, prefix='pessoa_form')

        endereco_form = EnderecoFormSet(
            instance=self.object, prefix='endereco_form')
        banco_form = BancoFormSet(instance=self.object, prefix='banco_form')
        documento_form = DocumentoFormSet(
            instance=self.object, prefix='documento_form')

        telefone_form = TelefoneFormSet(
            instance=self.object, prefix='telefone_form')
        email_form = EmailFormSet(instance=self.object, prefix='email_form')
        site_form = SiteFormSet(instance=self.object, prefix='site_form')

        if Telefone.objects.filter(pessoa_tel=self.object.pk).count():
            telefone_form.extra = 0
        if Endereco.objects.filter(pessoa_end=self.object.pk).count():
            endereco_form.extra = 0
        if Email.objects.filter(pessoa_email=self.object.pk).count():
            email_form.extra = 0
        if Site.objects.filter(pessoa_site=self.object.pk).count():
            site_form.extra = 0
        if Banco.objects.filter(pessoa_banco=self.object.pk).count():
            banco_form.extra = 0
        if Documento.objects.filter(pessoa_documento=self.object.pk).count():
            documento_form.extra = 0

        formsets = [telefone_form, email_form, site_form]

        # Caso Secretaria
        logo_file = kwargs.pop('logo_file', None)

        return self.render_to_response(self.get_context_data(form=form,
                                                             pessoa_form=pessoa_form,
                                                             endereco_form=endereco_form,
                                                             banco_form=banco_form,
                                                             documento_form=documento_form,
                                                             formsets=formsets,
                                                             logo_file=logo_file,
                                                             object=self.object))

    def post(self, request, form, *args, **kwargs):
        self.object = self.get_object()
        extra_forms = []

        endereco_form = EnderecoFormSet(
            request.POST, prefix='endereco_form', instance=self.object)
        banco_form = BancoFormSet(
            request.POST, prefix='banco_form', instance=self.object)
        documento_form = DocumentoFormSet(
            request.POST, prefix='documento_form', instance=self.object)

        telefone_form = TelefoneFormSet(
            request.POST, prefix='telefone_form', instance=self.object)
        email_form = EmailFormSet(
            request.POST, prefix='email_form', instance=self.object)
        site_form = SiteFormSet(
            request.POST, prefix='site_form', instance=self.object)

        formsets = [telefone_form, email_form, site_form]


        if (all(formset.is_valid() for formset in formsets) and
            endereco_form.is_valid() and
            banco_form.is_valid() and
            documento_form.is_valid() and
                all(extra_form.is_valid() for extra_form in extra_forms)):
            self.object = form.save(commit=False)
            self.object.save()
                # Remover pessoa fisica da DB se existir
            Pessoa.objects.filter(
                    pessoa_id=self.object.pk).delete()
            # Salvar informacoes endereco
            endereco_form.instance = self.object
            end = endereco_form.save()
            if len(end):
                self.object.endereco_padrao = end[0]
            # Salvar informacoes bancarias
            banco_form.instance = self.object
            ban = banco_form.save()
            if len(ban):
                self.object.banco_padrao = ban[0]
            # Salvar documentos adicionais
            documento_form.instance = self.object
            documento_form.save()

        logo_file = kwargs.pop('logo_file', None)

        pessoa_form = PessoaForm(
                request.POST, prefix='pessoa_form', instance=self.object)

        return self.form_invalid(form=form,
                                 pessoa_fisica_form=pessoa_form,
                                 endereco_form=endereco_form,
                                 banco_form=banco_form,
                                 documento_form=documento_form,
                                 formsets=formsets,
                                 logo_file=logo_file)
