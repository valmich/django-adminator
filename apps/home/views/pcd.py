from django.urls import reverse_lazy

from apps.home.forms.pcd import PcdForm
from apps.home.models.pcd import Pessoa

from .base import AdicionarPessoaView, PessoasListView, EditarPessoaView


class AdicionarPcdView(AdicionarPessoaView):
    template_name = "cadastro/pessoa_add.html"
    success_url = reverse_lazy('cadastro:listapcdview')
    success_message = "<b>%(nome)s </b>adicionado com sucesso."
    permission_codename = 'add_pcd'

    def get_context_data(self, **kwargs):
        context = super(AdicionarPcdView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR PcD'
        context['return_url'] = reverse_lazy('cadastro:listapcdsview')
        return context

    def get(self, request, *args, **kwargs):
        form = PcdForm(prefix='pcd_form')
        return super(AdicionarPcdView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = PcdForm(request.POST, request.FILES,
                           prefix='pcd_form', request=request)
        return super(AdicionarPcdView, self).post(request, form, *args, **kwargs)


class PcdListView(PessoasListView):
    template_name = 'cadastro/pessoa_list.html'
    model = Pessoa
    context_object_name = 'all_clientes'
    success_url = reverse_lazy('cadastro:listaclientesview')
    permission_codename = 'view_cliente'

    def get_context_data(self, **kwargs):
        context = super(PcdListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CLIENTES CADASTRADOS'
        context['add_url'] = reverse_lazy('cadastro:addpcdview')

        return context


class EditarPcdView(EditarPessoaView):
    form_class = PcdForm
    model = Pessoa
    template_name = "cadastro/pessoa_edit.html"
    success_url = reverse_lazy('cadastro:listapcdsview')
    success_message = " <b>%(nome_razao_social)s </b>editado com sucesso."
    permission_codename = 'change_pcd'

    def get_context_data(self, **kwargs):
        context = super(EditarPcdView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listapcdsview')
        
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form_class.prefix = "pcd_form"
        form = self.get_form(form_class)

        return super(EditarPcdView, self).get(request, form, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES,
                          prefix='pessoa_form', instance=self.object, request=request)
        return super(EditarPcdView, self).post(request, form, *args, **kwargs)
